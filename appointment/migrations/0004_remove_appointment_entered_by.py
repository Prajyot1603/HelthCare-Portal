# Generated by Django 4.2.2 on 2023-07-08 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_alter_appointment_date_of_schedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Entered_by',
        ),
    ]
