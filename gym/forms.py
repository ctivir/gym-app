from django import forms

from .models import Applicant


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        # exclude = ['applicant_id']
        fields = ('applicant_id', 'name', 'surname', 'gender', 'age', 'occupation', 'address', 'phone_number1',
                  'phone_number2', 'phone_emergence', 'email', 'plan')

        list_filter = ('name', 'age')

