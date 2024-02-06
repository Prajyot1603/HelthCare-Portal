# Generated by Django 4.2.2 on 2023-07-28 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0008_alter_products_enteredby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='EnteredBy',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
