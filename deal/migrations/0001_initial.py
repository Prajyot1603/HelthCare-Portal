# Generated by Django 4.2.2 on 2023-07-07 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_alter_doctors_doctor_specialisation'),
        ('product', '0002_rename_image_products_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=1)),
                ('Entered_by', models.CharField(max_length=100)),
                ('Doctor_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctors')),
                ('Product_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            options={
                'db_table': 'Deal',
            },
        ),
    ]
