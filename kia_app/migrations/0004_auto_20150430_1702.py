# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kia_app', '0003_auto_20150430_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='grade',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
