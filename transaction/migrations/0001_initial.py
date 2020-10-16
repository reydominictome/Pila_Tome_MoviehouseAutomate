# Generated by Django 3.1 on 2020-10-08 12:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0005_auto_20201008_2017'),
        ('customer', '0025_auto_20201008_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('date_of_transaction', models.DateField(default=datetime.datetime(2020, 10, 8, 20, 17, 4, 494124))),
                ('room_no', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='customer.customer')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Movie', to='movie.movie')),
            ],
            options={
                'db_table': 'Transaction',
            },
        ),
    ]
