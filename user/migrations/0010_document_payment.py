# Generated by Django 4.1.5 on 2023-01-13 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_upload_file_medical_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Document', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_payment', models.IntegerField(null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.appointments')),
            ],
        ),
    ]
