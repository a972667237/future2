# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-26 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180226_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider_info',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='\u63cf\u8ff0'),
        ),
    ]
