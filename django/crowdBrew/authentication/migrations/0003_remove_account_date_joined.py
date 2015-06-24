# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_account_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='date_joined',
        ),
    ]
