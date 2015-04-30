# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kia_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='grade',
            field=models.CharField(max_length=b'50', blank=True),
        ),
    ]
