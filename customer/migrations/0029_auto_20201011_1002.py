# Generated by Django 3.1 on 2020-10-11 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0028_auto_20201011_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 10, 11, 10, 2, 16, 183004)),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 11, 10, 2, 16, 183004)),
        ),
    ]