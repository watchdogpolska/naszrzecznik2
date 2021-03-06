# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 03:00
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='signatures.Category', verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petition',
            name='giodo_text',
            field=models.TextField(default='', verbose_name='Privacy aggrement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_text',
            field=models.TextField(default='', verbose_name='Newsletter aggrement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signature',
            name='newsletter',
            field=models.BooleanField(default=False, verbose_name='Newsletter acceptation'),
        ),
        migrations.AddField(
            model_name='signature',
            name='privacy',
            field=models.BooleanField(default=False, verbose_name='Privacy acceptation'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'title', unique=True, verbose_name='Slug'),
        ),
    ]
