# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-09 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ussurl',
            name='timestamp',
        ),
    ]
