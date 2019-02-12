from django.contrib import admin
from .models import Applicant, Payment, Plan

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Payment)
admin.site.register(Plan)