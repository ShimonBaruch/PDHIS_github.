# Generated by Django 4.1.3 on 2022-12-25 15:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSecretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('Role', models.CharField(choices=[('1', 'secretary'), ('2', 'secretary'), ('1', 'secretary')], default='Secretary', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=9)),
                ('phone_number', models.CharField(max_length=10)),
                ('Role', models.CharField(choices=[('1', 'patient'), ('1', 'patient')], default='patient', max_length=1)),
                ('priority', models.IntegerField(default=1)),
                ('user_patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(choices=[('1', 'doctor'), ('1', 'doctor')], default='doctor', max_length=1)),
                ('department', models.CharField(choices=[('1', 'Otorhinolaryngology'), ('2', 'Cardiology'), ('3', 'Oncology')], max_length=50)),
                ('user_doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('appointment_end', models.BooleanField(default=False)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='user.userdoctor')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='user.userpatient')),
            ],
        ),
    ]