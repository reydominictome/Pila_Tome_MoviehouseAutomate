# Generated by Django 3.1 on 2020-09-19 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20200919_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 19, 21, 39, 58, 102900)),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 19, 21, 39, 58, 101902)),
        ),
    ]
