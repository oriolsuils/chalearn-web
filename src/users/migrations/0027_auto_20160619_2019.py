# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_remove_event_parent_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Dataset'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=users.models.user_avatar_path),
        ),
    ]