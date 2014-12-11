# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141209_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('company_name', models.CharField(max_length=200, verbose_name='Company Name')),
                ('contact_name', models.CharField(max_length=200, verbose_name='Contact Name', null=True)),
                ('contact_email', models.EmailField(max_length=75, verbose_name='Contact Email', null=True)),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Contact Phone', null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, verbose_name='date updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_target',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 22, 14, 42, 438762, tzinfo=utc), auto_now=True, verbose_name='date updated'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='company',
            field=models.ForeignKey(to='app.Company', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='position',
            field=models.TextField(default='', verbose_name='What kind of Opportunity are you looking for?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True, verbose_name='date updated'),
            preserve_default=True,
        ),
    ]
