# Generated by Django 4.2.2 on 2023-07-27 15:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_products_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Product_price',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
