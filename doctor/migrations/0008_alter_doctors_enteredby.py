# Generated by Django 4.2.2 on 2023-07-29 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0007_alter_doctors_doctor_specialisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='EnteredBy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
