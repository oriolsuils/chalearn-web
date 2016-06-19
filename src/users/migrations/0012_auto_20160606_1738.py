# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20160606_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_relation',
            name='event',
        ),
        migrations.RemoveField(
            model_name='event_relation',
            name='relation',
        ),
        migrations.AddField(
            model_name='event_relation',
            name='challenge_relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='challenge_relation', to='users.Challenge'),
        ),
        migrations.AddField(
            model_name='event_relation',
            name='event_associated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_associated', to='users.Event'),
        ),
        migrations.AddField(
            model_name='event_relation',
            name='issue_relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issue_relation', to='users.Special_Issue'),
        ),
        migrations.AddField(
            model_name='event_relation',
            name='workshop_relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workshop_relation', to='users.Workshop'),
        ),
    ]