# Generated by Django 5.0.4 on 2024-06-13 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_listing_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='test',
        ),
    ]
