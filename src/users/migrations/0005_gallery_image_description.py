# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 14:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160531_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_image',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]