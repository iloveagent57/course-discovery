# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170830_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='lms_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='LMS URL'),
        ),
    ]