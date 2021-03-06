# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-19 16:53
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def create_identifier(apps, schema_editor):

    Task = apps.get_model('tasks', 'Task')

    for obj in Task.objects.all():
        if not obj.key:
            obj.key = slugify(obj.title_en)
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_refactoring'),
    ]

    operations = [
        migrations.RunPython(create_identifier),
    ]
