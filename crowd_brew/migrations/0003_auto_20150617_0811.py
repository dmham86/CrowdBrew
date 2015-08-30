# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowd_brew', '0002_auto_20150520_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='tasting',
            field=models.ForeignKey(related_name='keywords', to='crowd_brew.Tasting'),
            preserve_default=True,
        ),
    ]
