# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaffeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.TextField()),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'caffe_model',
            },
        ),
    ]
