# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi', '0010_graphmeasure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selectsub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_select', models.CharField(max_length=20)),
            ],
        ),
    ]
