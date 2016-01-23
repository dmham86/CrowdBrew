# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20150624_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(unique=True, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9\\_]{4,20}$', message=b'Username cannot contain spaces or special characters except _', code=b'invalid_username')]),
        ),
    ]
