# Generated by Django 2.0.9 on 2019-03-10 15:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('applicant_id', models.IntegerField(default='9982912', unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('surname', models.CharField(max_length=100, verbose_name='Apelido')),
                ('gender', models.CharField(choices=[('1', 'Masculino'), ('2', 'Feminino'), (' ', 'Nao especificado')], max_length=254)),
                ('age', models.DateField(verbose_name='Data de nascimento')),
                ('occupation', models.CharField(max_length=100, verbose_name='Ocupcao')),
                ('address', models.CharField(max_length=100, verbose_name='Morada')),
                ('address1', models.CharField(max_length=100, verbose_name='Bairro')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('phone_number1', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number2', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_emergence', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('1', 'activo'), ('2', 'desactivo')], help_text='status', max_length=254)),
                ('plan', models.CharField(choices=[('1', 'Completo'), ('2', 'Mosculacao'), ('3', 'Aulas em grupo'), ('4', 'Modalidade taykwond')], help_text='Plano', max_length=254)),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-application_date'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('total_discount_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2019, 4, 9, 15, 7, 30, 855323), verbose_name='Data de Vencimento')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='gym.Applicant')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Test', max_length=100, verbose_name='Pacote')),
                ('plan_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descrição')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='gym.Plan'),
        ),
    ]
