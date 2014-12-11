# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20141209_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date updated'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date updated'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resume',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date updated'),
            preserve_default=True,
        ),
    ]
