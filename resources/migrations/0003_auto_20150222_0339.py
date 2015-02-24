# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20150220_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='left',
            field=models.IntegerField(default=10, verbose_name='Left'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='top',
            field=models.IntegerField(default=10, verbose_name='Top'),
            preserve_default=True,
        ),
    ]
