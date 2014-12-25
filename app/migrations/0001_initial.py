# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bootstrap_theme', models.CharField(verbose_name='Twitter Bootstrap image', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(verbose_name='Company Name', max_length=200)),
                ('contact_name', models.CharField(verbose_name='Contact Name', null=True, max_length=200, blank=True)),
                ('contact_email', models.EmailField(verbose_name='Contact Email', null=True, max_length=75, blank=True)),
                ('contact_phone', models.CharField(verbose_name='Contact Phone', null=True, max_length=20, blank=True)),
                ('last_updated', models.DateTimeField(verbose_name='date updated', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=100)),
                ('street_address2', models.CharField(null=True, max_length=100, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(null=True, max_length=100, blank=True)),
                ('last_updated', models.DateTimeField(verbose_name='date updated', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(verbose_name='School Name', max_length=200)),
                ('school_location', models.CharField(verbose_name='School Location', max_length=200)),
                ('coursework', models.TextField(verbose_name='School Name', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_default', models.NullBooleanField(verbose_name='Is This the Default Resume you want to show?')),
                ('about_me', tinymce.models.HTMLField(verbose_name='About Me')),
                ('position', models.CharField(verbose_name='What kind of Opportunity are you looking for?', max_length=200)),
                ('description', tinymce.models.HTMLField(verbose_name='Vision Statement:', null=True, blank=True)),
                ('last_updated', models.DateTimeField(verbose_name='date updated', auto_now_add=True)),
                ('company', models.ForeignKey(null=True, to='app.Company')),
                ('contact', models.ForeignKey(null=True, to='app.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_name', models.CharField(verbose_name='Skill Name', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_current', models.NullBooleanField(verbose_name='Is Current Position')),
                ('place_of_work', models.CharField(verbose_name='Place Of Work', max_length=200)),
                ('location', models.CharField(verbose_name='Location', max_length=200)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date', null=True, blank=True)),
                ('position', models.CharField(verbose_name='Position Title', null=True, max_length=200, blank=True)),
                ('work_description', tinymce.models.HTMLField(verbose_name='Description of Position', null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_proficiency_level', models.IntegerField(choices=[(0, 'Minimal Exposure'), (1, 'Working Knowledge'), (2, 'Expert'), (3, 'Ninja')], default=1)),
                ('skill', models.ForeignKey(to='app.Skill')),
                ('work_history', models.ForeignKey(to='app.WorkHistory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='workhistory',
            name='work_skills',
            field=models.ManyToManyField(verbose_name='Skills Used', null=True, to='app.Skill', through='app.WorkSkill', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='work_histories',
            field=models.ManyToManyField(null=True, to='app.WorkHistory', blank=True),
            preserve_default=True,
        ),
    ]
