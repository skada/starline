# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='Start')),
                ('end', models.DateField(verbose_name='End')),
                ('state', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Planning'), (1, 'Ready'), (2, 'In progress'), (3, 'Closed')], verbose_name='State')),
                ('compound', models.ForeignKey(to='resources.Compound')),
            ],
            options={
                'verbose_name_plural': 'Batches',
                'verbose_name': 'Batch',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Placements',
                'verbose_name': 'Placement',
            },
            bases=(models.Model,),
        ),
    ]
