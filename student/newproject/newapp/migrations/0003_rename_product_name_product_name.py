# Generated by Django 5.0.7 on 2024-07-21 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_product_price_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
