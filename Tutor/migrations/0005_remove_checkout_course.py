# Generated by Django 4.0 on 2024-12-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0004_remove_checkout_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='course',
        ),
    ]
