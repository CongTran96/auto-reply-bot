# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply_comment_facebook', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]