# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 02:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170116_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='publicar',
        ),
    ]
