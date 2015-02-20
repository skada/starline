# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=75, verbose_name='email address', unique=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('user_type', models.SmallIntegerField(choices=[(0, 'Admin'), (1, 'Main instructor'), (2, 'Doctor'), (3, 'Tutor'), (4, 'Parent')], db_index=True, verbose_name='User type')),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_query_name='user')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_query_name='user')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ('email',),
                'verbose_name': 'User',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'Kids',
                'verbose_name': 'Kid',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KidGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='SLug')),
            ],
            options={
                'verbose_name_plural': 'Kid groups',
                'verbose_name': 'Kid group',
            },
            bases=(models.Model,),
        ),
    ]
