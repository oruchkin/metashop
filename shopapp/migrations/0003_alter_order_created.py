# Generated by Django 4.1.2 on 2022-10-11 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_car_model_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 13, 22, 33, 359977, tzinfo=datetime.timezone.utc), verbose_name='заказ создан'),
        ),
    ]