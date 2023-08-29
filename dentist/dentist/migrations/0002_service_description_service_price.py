# Generated by Django 4.2.4 on 2023-08-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]