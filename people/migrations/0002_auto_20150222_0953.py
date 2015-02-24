# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryMedicalCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medicine', models.CharField(max_length=100, null=True, verbose_name='Medicine', blank=True)),
                ('dosage', models.CharField(max_length=50, null=True, verbose_name='Dosage', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('kid', models.ForeignKey(to='people.Kid')),
            ],
            options={
                'verbose_name': 'Entry medical check',
                'verbose_name_plural': 'Entry medical checks',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kid',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
    ]
