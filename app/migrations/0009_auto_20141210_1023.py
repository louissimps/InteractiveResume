# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20141209_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('skill_name', models.CharField(verbose_name='Skill Name', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillProficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('skill_proficiency_level', models.IntegerField(choices=[(1, 'No Experience'), (2, 'Minimal Exposure'), (3, 'Working Knowledge'), (4, 'Expert'), (5, 'Ninja')], default=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('place_of_work', models.CharField(verbose_name='Place Of Work', max_length=200)),
                ('location', models.CharField(verbose_name='Location', max_length=200)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date', blank=True, null=True)),
                ('work_description', models.TextField(verbose_name='Description of Position', blank=True, null=True)),
                ('skills', models.ManyToManyField(to='app.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_proficiency',
            field=models.ForeignKey(to='app.SkillProficiency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='work_histories',
            field=models.ManyToManyField(blank=True, to='app.WorkHistory', null=True),
            preserve_default=True,
        ),
    ]
