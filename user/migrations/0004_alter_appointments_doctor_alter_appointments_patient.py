# Generated by Django 4.1.3 on 2023-01-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_appointments_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.userdoctor'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.userpatient'),
        ),
    ]
