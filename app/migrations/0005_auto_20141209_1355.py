# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_resume_resume_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='resume',
        ),
        migrations.AddField(
            model_name='resume',
            name='contact',
            field=models.ForeignKey(to='app.Contact', null=True),
            preserve_default=True,
        ),
    ]
