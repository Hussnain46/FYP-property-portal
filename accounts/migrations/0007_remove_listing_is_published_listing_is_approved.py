# Generated by Django 5.0.4 on 2024-06-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_listing_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='is_published',
        ),
        migrations.AddField(
            model_name='listing',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
