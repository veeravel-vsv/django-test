# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_polls', '0002_auto_20161111_2003'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='LoginUser',
        ),
    ]