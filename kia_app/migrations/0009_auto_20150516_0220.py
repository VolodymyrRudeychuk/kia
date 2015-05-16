# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kia_app', '0008_category_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='token',
        ),
        migrations.AddField(
            model_name='statistic',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
