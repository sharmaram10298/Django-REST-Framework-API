# Generated by Django 4.2.1 on 2023-06-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_employee_address_employee_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='pincode',
            field=models.CharField(default='400103', max_length=100),
        ),
    ]
