# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-27 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(default=b'', max_length=3)),
            ],
        ),
    ]
