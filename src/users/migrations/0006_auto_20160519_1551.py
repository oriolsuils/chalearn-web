# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 15:51
from __future__ import unicode_literals

import ajaximage.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160513_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
    ]
