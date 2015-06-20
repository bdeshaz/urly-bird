# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarker', '0002_auto_20150619_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='s_code',
            field=models.CharField(max_length=200),
        ),
    ]
