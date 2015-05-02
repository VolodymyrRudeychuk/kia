# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kia_app', '0006_auto_20150502_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='grade',
        ),
    ]
