from django import forms

from .models import Applicant, Payment, Plan


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        # exclude = ['applicant_id']
        fields = ('name', 'surname', 'gender', 'age', 'occupation', 'address', 'phone_number1',
                  'phone_number2', 'phone_emergence', 'email', 'plan')

        list_filter = ('name', 'age')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'