# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.sites.models import Site
from django.db.utils import ProgrammingError

def set_site(apps, schema_editor):
    try:
        site = Site.objects.get(id=1)
        site.name = "CrowdBrew"
        site.domain = "crowdbrew.local"
        site.save()
    except ProgrammingError:
        print "Unable to create CrowdBrew site"

class Migration(migrations.Migration):

    dependencies = [
        ('crowd_brew', '0003_auto_20150617_0811'),
    ]

    operations = [
        migrations.RunPython(set_site),
    ]
