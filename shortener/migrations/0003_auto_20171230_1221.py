# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-30 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20171226_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ussurl',
            name='url',
            field=models.CharField(max_length=120, validators=[shortener.validators.validate_url]),
        ),
    ]