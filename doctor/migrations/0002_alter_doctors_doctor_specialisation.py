# Generated by Django 4.2.2 on 2023-07-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='Doctor_Specialisation',
            field=models.CharField(choices=[('Chest', 'Chest'), ('Heart', 'Heart'), ('General', 'General'), ('Orthopaedic', 'Orthopaedic')], max_length=50),
        ),
    ]
