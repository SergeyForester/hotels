# Generated by Django 2.2.2 on 2020-06-06 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0003_auto_20200530_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='date_of_expiry',
            field=models.DateField(default=datetime.datetime(2021, 6, 6, 16, 12, 40, 524696)),
        ),
    ]
