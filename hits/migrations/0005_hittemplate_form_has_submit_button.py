# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hits', '0004_auto_20180927_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='hittemplate',
            name='form_has_submit_button',
            field=models.BooleanField(default=False),
        ),
    ]
