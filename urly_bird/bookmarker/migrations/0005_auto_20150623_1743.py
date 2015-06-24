# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarker', '0004_auto_20150620_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='creator',
            field=models.ForeignKey(related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]