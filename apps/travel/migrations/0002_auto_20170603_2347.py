# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='travelers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trip_travelers', to='LogReg.userDB'),
        ),
    ]
