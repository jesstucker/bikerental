# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_group_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='catg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Category'),
        ),
    ]