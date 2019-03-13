from django import forms

from .models import Applicant, Payment, Plan


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        # exclude = ['applicant_id']
        fields = ('name', 'surname', 'gender', 'age', 'occupation', 'address', 'address1', 'city', 'phone_number1',
                  'phone_number2', 'phone_emergence', 'email', 'payment_plan')

        list_filter = ('name', 'age')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('applicant', 'plan', 'total_amount', 'total_discount_amount')


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('name', 'amount', 'plan_description')
