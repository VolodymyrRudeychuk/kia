# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kia_app', '0011_message_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='grade',
            field=models.IntegerField(choices=[(0, b'Ages 4-5'), (1, b'Grade 1'), (2, b'Grade 2'), (3, b'Grade 3'), (4, b'Grade 4'), (5, b'Grade 5'), (6, b'Grade 6'), (7, b'Grade 7'), (8, b'Grade 8'), (9, b'Grade 9')]),
        ),
    ]
