# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcebase',
            options={'verbose_name': 'Resource Base', 'verbose_name_plural': 'Resources Bases'},
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
            preserve_default=True,
        ),
    ]
