import random
import uuid
from datetime import datetime, timedelta
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from gym.choices import GENDER_CHOICES, PLAN_CHOICES, STATUS_CHOICES, PAY_CHOICES


class Applicant(models.Model):

    def pin():
        return ''.join(random.choice('0123456789') for _ in range(7))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    applicant_id = models.IntegerField(unique=True, default=pin())

    name = models.CharField(max_length=100, verbose_name="Nome")

    surname = models.CharField(max_length=100, verbose_name="Apelido")

    gender = models.CharField(
        max_length=254,
        choices=GENDER_CHOICES,
        # help_text='Genero'
    )

    age = models.DateField(verbose_name="Data de nascimento")

    occupation = models.CharField(max_length=100, verbose_name="Ocupcao")

    address = models.CharField(max_length=100, verbose_name="Morada")

    address1 = models.CharField(max_length=100, verbose_name="Bairro")

    city = models.CharField(max_length=100, verbose_name="Cidade")

    phone_number1 = models.CharField(max_length=100, null=True, blank=True)

    phone_number2 = models.CharField(max_length=100, null=True, blank=True)

    phone_emergence = models.CharField(max_length=100, null=True, blank=True)

    email = models.CharField(max_length=100, null=True, blank=True)

    status = models.CharField(
        max_length=254,
        choices=STATUS_CHOICES,
        help_text='status',
        default='1',
    )
    payment_plan = models.CharField(
        max_length=254,
        choices=PAY_CHOICES,
        help_text='Plano'
    )

    application_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-application_date']

    def __str__(self):
        return self.name


# Pacotes
class Plan(models.Model):

    name = models.CharField(max_length=100, verbose_name="Pacote")

    amount = models.DecimalField(decimal_places=2, max_digits=100)

    plan_description = models.CharField(max_length=100, verbose_name="Descrição", null=True, blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Payment(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    applicant = models.ForeignKey(Applicant, on_delete=CASCADE, related_name='payment')

    plan = models.ForeignKey(Plan, on_delete=CASCADE)

    total_amount = models.DecimalField(decimal_places=2, max_digits=100)

    total_discount_amount = models.DecimalField(decimal_places=2, max_digits=100)

    created_date = models.DateTimeField(default=datetime.now)

    end_date = models.DateTimeField(default=datetime.now()+timedelta(days=30), verbose_name="Data de Vencimento")

    def __str__(self):
        return self.plan
