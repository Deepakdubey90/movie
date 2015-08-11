# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('popularity', models.DecimalField(decimal_places=6, default=None, verbose_name='Popularity', null=True, max_digits=20, blank=True)),
                ('director', models.CharField(null=True, max_length=40, verbose_name='Director')),
                ('imdb_score', models.DecimalField(decimal_places=6, default=None, verbose_name='IMDB Score', null=True, max_digits=20, blank=True)),
                ('name', models.CharField(null=True, max_length=30, verbose_name='Name')),
                ('deleted_on', models.DateTimeField(default=None, null=True, blank=True, verbose_name='Deleted On')),
                ('genre', models.ManyToManyField(blank=True, to='genre.Type')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
