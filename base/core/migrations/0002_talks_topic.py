# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-13 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talks',
            name='topic',
            field=models.CharField(choices=[('team_culture', 'Team Culture'), ('project_management', 'Project Management'), ('marketing', 'Marketing'), ('tech', 'Technology'), ('design', 'Design')], default='card', max_length=100),
        ),
    ]