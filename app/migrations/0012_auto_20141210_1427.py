# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20141210_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workskill',
            name='skill_proficiency',
        ),
        migrations.DeleteModel(
            name='SkillProficiency',
        ),
        migrations.AddField(
            model_name='workskill',
            name='skill_proficiency_level',
            field=models.IntegerField(choices=[(1, 'No Experience'), (2, 'Minimal Exposure'), (3, 'Working Knowledge'), (4, 'Expert'), (5, 'Ninja')], default=3),
            preserve_default=True,
        ),
    ]
