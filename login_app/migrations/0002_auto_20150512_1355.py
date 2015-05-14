# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(max_length=100, choices=[(b'CSE', b'Computer Science And Engineering'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics And Communication Engineering'), (b'MIED', b'Metalurgical Engineering'), (b'CE', b'Civil Engineering'), (b'ME', b'Mechanical Engineering')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='enrollment',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(primary_key=True, serialize=False, to='login_app.user'),
        ),
    ]
