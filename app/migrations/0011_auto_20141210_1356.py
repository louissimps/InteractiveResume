# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20141210_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workhistory',
            name='skills',
        ),
        migrations.AddField(
            model_name='workskill',
            name='work_history',
            field=models.ForeignKey(blank=True, to='app.WorkHistory', null=True),
            preserve_default=True,
        ),
    ]
