# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-06 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forum.Thread', verbose_name='Tópico'),
            preserve_default=False,
        ),
    ]
