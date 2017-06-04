# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogReg', '0002_auto_20170603_2337'),
        ('travel', '0002_auto_20170603_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='travelers',
        ),
        migrations.AddField(
            model_name='trip',
            name='travelers',
            field=models.ManyToManyField(related_name='trip_travelers', to='LogReg.userDB'),
        ),
    ]