# Generated by Django 4.2.2 on 2023-07-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_remove_appointment_entered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Entered_by',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
