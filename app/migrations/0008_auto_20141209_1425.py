# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20141209_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_email',
            field=models.EmailField(max_length=75, blank=True, null=True, verbose_name='Contact Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_name',
            field=models.CharField(max_length=200, blank=True, null=True, verbose_name='Contact Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_phone',
            field=models.CharField(max_length=20, blank=True, null=True, verbose_name='Contact Phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resume',
            name='position',
            field=models.CharField(max_length=200, verbose_name='What kind of Opportunity are you looking for?'),
            preserve_default=True,
        ),
    ]
