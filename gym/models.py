import uuid
from django.contrib import admin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from gym.choices import GENDER_CHOICES, PLAN_CHOICES, STATUS_CHOICES


# class AggregateModels(AuthStampedMode):
#     uri = models.CharField(max_length=254)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     class Meta:
#         abstract = True


class Applicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    applicant_id = models.CharField(
        max_length=9,
        unique=False,
        validators=[MinLengthValidator(7, 'codigo com 9 digitos'), MinLengthValidator(7, 'codigo com 9 digitos')])

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
        help_text='status'
    )
    plan = models.CharField(
        max_length=254,
        choices=PLAN_CHOICES,
        help_text='Plano'
    )


    application_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-application_date']

    def __str__(self):
        return self.name


class Payment(models.Model):
    applicant = models.ForeignKey('gym.Applicant', on_delete=models.CASCADE, related_name='payment')

    plan = models.ForeignKey('gym.Plan', on_delete=models.CASCADE, related_name='payment')

    payment_type = models.CharField(
        max_length=254,
        choices=PLAN_CHOICES,
        help_text='Pacote'
    )

    total_amount = models.DecimalField(decimal_places=3, max_digits=100)

    total_discount_amount = models.DecimalField(decimal_places=2, max_digits=100)

    author = models.CharField(max_length=200)

    created_date = models.DateTimeField(default=timezone.now)


class Plan(models.Model):
    author = models.CharField(max_length=200)

    plan_discount = models.FloatField()

    plan_description = models.CharField(max_length=100, null=True, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
