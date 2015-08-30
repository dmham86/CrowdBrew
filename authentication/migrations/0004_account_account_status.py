# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_account_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_status',
            field=models.CharField(default=b'New', max_length=10, choices=[(b'New', b'New'), (b'Active', b'Active'), (b'Disabled', b'Disabled')]),
            preserve_default=True,
        ),
    ]
