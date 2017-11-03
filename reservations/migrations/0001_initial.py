# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0010_auto_20171028_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begins', models.DateTimeField()),
                ('ends', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.IndividualItem')),
            ],
        ),
    ]
