from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from gym.forms import ApplicantForm, PaymentForm, PlanForm
from gym.models import Applicant, Plan


@login_required(login_url='/accounts/login/')
def applicant_list(request):
    applicants = Applicant.objects.filter(application_date__lte=timezone.now()).order_by('application_date')
    return render(request, 'applicant/applicant_list.html', {'applicants': applicants})


@login_required()
def applicant_detail(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    return render(request, 'applicant/applicant_detail.html', {'applicant': applicant})


@login_required()
def applicant_new(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return redirect('gym:applicant_detail', pk=applicant.pk)
    else:
        form = ApplicantForm()
    return render(request, 'applicant/applicant_edit.html', {'form': form})


@login_required()
def applicant_edit(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == "POST":
        form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return redirect('gym:applicant_detail', pk=applicant.pk)
    else:
        form = ApplicantForm(instance=applicant)
        return render(request, 'applicant/applicant_edit.html', {'form': form})


@login_required()
def applicant_pay(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.save()
            return redirect('gym:applicant_pay', pk=pay.pk)
    else:
        form = PaymentForm()
    return render(request, 'payment/applicant_pay.html', {'form': form})


@login_required()
def plan_new(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.save()
            return redirect('gym:plan_list')
    else:
        form = PlanForm()
    return render(request, 'payment/plan.html', {'form': form})

@login_required()
def plan_list(request):
    plans = Plan.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'payment/plan_list.html', {'plans': plans})
