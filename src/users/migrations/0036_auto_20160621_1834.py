# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_dataset_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_dataset_profile1', to='users.Dataset')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_profile_dataset1', to='users.Profile')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Role')),
            ],
        ),
        migrations.AlterField(
            model_name='proposal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile'),
        ),
    ]
