# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20150220_1133'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('start', models.DateField(verbose_name='Start')),
                ('end', models.DateField(verbose_name='End')),
                ('state', models.PositiveSmallIntegerField(verbose_name='State', choices=[(0, 'Planning'), (1, 'Ready'), (2, 'In progress'), (3, 'Closed')], default=0)),
                ('compound', models.ForeignKey(to='resources.Compound')),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('batch', models.ForeignKey(to='planning.Batch')),
                ('compound', models.ForeignKey(blank=True, null=True, to='resources.Compound')),
                ('kid', models.ForeignKey(blank=True, null=True, to='people.Kid')),
                ('resource', models.ForeignKey(to='resources.Resource')),
            ],
            options={
                'verbose_name': 'Placement',
                'verbose_name_plural': 'Placements',
            },
            bases=(models.Model,),
        ),
    ]
