# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggedvideo',
            name='category',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='taggedvideo',
            unique_together=set([('category', 'tag')]),
        ),
    ]