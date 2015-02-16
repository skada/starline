# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceBase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, blank=True, to='resources.ResourceBase')),
            ],
            options={
                'verbose_name_plural': 'Resources',
                'verbose_name': 'Resource',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('resources.resourcebase',),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('resources.resourcebase',),
        ),
    ]
