# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 10:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180222_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval_log',
            name='approve_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 22, 10, 56, 17, 273084)),
        ),
    ]