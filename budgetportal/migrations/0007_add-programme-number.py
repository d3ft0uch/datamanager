# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetportal', '0006_add-programmes'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='programme_number',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='programme',
            unique_together=set([('department', 'slug'), ('department', 'name'), ('department', 'programme_number')]),
        ),
    ]
