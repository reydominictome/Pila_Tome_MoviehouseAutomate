# Generated by Django 3.1 on 2020-09-23 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_auto_20200923_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 10, 16, 40, 316773)),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 10, 16, 40, 315739)),
        ),
    ]