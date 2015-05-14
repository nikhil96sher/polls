# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20150512_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Nikhil', max_length=100),
            preserve_default=False,
        ),
    ]
