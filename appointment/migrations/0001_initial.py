# Generated by Django 4.2.2 on 2023-07-04 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_Schedule', models.DateField(auto_now_add=True)),
                ('Time_of_Schedule', models.TimeField(auto_now_add=True)),
                ('Entered_by', models.CharField(max_length=100)),
                ('Doctor_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctors')),
            ],
            options={
                'db_table': 'Appointment',
            },
        ),
    ]
