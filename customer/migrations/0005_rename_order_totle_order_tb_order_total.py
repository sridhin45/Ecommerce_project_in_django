# Generated by Django 5.1.1 on 2024-11-14 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_order_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_tb',
            old_name='order_totle',
            new_name='order_total',
        ),
    ]
