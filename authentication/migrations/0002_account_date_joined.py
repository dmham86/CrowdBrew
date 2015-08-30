# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 12, 44, 9, 888000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
