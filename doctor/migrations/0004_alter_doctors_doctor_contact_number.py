# Generated by Django 4.2.2 on 2023-07-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctors_doctor_specialisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='Doctor_Contact_Number',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]