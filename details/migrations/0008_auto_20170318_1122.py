# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_auto_20170317_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Book Name'),
        ),
        migrations.AlterField(
            model_name='bookrating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_rating', to='details.Book'),
        ),
        migrations.AlterField(
            model_name='bookrating',
            name='rating',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
