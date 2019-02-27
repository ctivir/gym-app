# Generated by Django 2.0.9 on 2019-02-27 22:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_auto_20190227_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='applicant_id',
            field=models.IntegerField(default='9541083', max_length=7, unique=True, validators=[django.core.validators.MinLengthValidator(7, 'codigo com 9 digitos'), django.core.validators.MinLengthValidator(7, 'codigo com 9 digitos')]),
        ),
    ]
