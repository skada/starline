# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.SmallIntegerField(default=4, db_index=True, verbose_name='User type', choices=[(0, 'Admin'), (1, 'Main instructor'), (2, 'Doctor'), (3, 'Tutor'), (4, 'Parent')]),
            preserve_default=False,
        ),
    ]
