# Generated by Django 3.1 on 2020-09-19 12:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0004_auto_20200918_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('barangay', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('birth_date', models.DateField(default=datetime.datetime(2020, 9, 19, 20, 56, 32, 93527))),
                ('gender', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('spouse_name', models.CharField(blank=True, max_length=50)),
                ('spouse_occupation', models.CharField(blank=True, max_length=50)),
                ('no_of_children', models.IntegerField()),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.person')),
                ('date_registered', models.DateField(default=datetime.datetime(2020, 9, 19, 20, 56, 32, 93527))),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'db_table': 'Customer',
            },
            bases=('customer.person',),
        ),
    ]
