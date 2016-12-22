# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_polls', '0003_loginuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]