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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.SmallIntegerField(db_index=True, choices=[(0, 'Admin'), (1, 'Main instructor'), (2, 'Doctor'), (3, 'Tutor'), (4, 'Parent')], verbose_name='User type')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', blank=True, help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('email',),
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('non_swimmer', models.BooleanField(default=False, verbose_name='Non swimmer')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Kid groups',
                'verbose_name': 'Kid group',
            },
            bases=(models.Model,),
        ),
    ]
