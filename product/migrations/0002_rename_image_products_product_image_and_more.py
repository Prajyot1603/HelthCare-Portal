# Generated by Django 4.2.2 on 2023-07-01 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='Product_image',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='Product_name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='Product_price',
        ),
    ]
