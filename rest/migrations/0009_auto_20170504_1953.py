# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_auto_20170504_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, to='rest.Symbol'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='symbol',
            field=models.ForeignKey(db_column='symbol', on_delete=django.db.models.deletion.CASCADE, related_name='coins', to='rest.Symbol'),
        ),
    ]