# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20150623_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='bookmark',
            field=models.ForeignKey(to='bookmarker.Bookmark', related_name='clicks'),
        ),
        migrations.AlterField(
            model_name='click',
            name='clicker',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
