# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0002_auto_20170315_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]