# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0014_auto_20170507_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='name',
            field=models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='symbol',
            field=models.CharField(db_index=True, max_length=16),
        ),
    ]
