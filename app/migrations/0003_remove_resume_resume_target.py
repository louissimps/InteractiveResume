# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141209_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='resume_target',
        ),
    ]
