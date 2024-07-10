# Generated by Django 5.0.4 on 2024-05-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
