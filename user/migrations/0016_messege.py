# Generated by Django 4.1.5 on 2023-01-14 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_userdoctor_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='messege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messege', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.userdoctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.userpatient')),
                ('secretary', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.usersecretary')),
            ],
        ),
    ]
