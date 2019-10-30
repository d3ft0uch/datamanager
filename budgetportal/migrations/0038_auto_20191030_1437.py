# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-30 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("budgetportal", "0037_homepage")]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="call_to_action_link_target",
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name="homepage",
            name="primary_button_target",
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name="homepage",
            name="secondary_button_target",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
