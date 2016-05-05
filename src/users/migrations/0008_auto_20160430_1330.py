# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160430_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=users.models.user_avatar_path),
        ),
    ]
