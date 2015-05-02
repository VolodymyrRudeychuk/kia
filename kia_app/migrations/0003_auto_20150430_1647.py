# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kia_app', '0002_category_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='grade',
        ),
        migrations.AddField(
            model_name='grade',
            name='category',
            field=models.ForeignKey(to='kia_app.Category'),
        ),
    ]
