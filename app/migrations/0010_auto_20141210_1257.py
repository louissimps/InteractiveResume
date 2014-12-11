# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20141210_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSkill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('skill', models.ForeignKey(null=True, blank=True, to='app.Skill')),
                ('skill_proficiency', models.ForeignKey(null=True, blank=True, to='app.SkillProficiency')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill_proficiency',
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='skills',
            field=models.ManyToManyField(to='app.WorkSkill'),
            preserve_default=True,
        ),
    ]
