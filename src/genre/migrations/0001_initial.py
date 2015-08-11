# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('slug', models.SlugField(max_length=16, verbose_name='Slug')),
                ('genre', models.CharField(db_index=True, max_length=16, verbose_name='Genre')),
            ],
        ),
    ]
