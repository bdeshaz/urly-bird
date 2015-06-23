# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='clicker',
            field=models.ForeignKey(related_name='clicks', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
