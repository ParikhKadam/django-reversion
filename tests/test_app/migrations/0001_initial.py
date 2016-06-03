# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-03 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reversion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('revision', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reversion.Revision')),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='v1', max_length=191)),
            ],
        ),
    ]