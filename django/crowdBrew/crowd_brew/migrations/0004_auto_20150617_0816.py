# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.sites.models import Site
from django.db.utils import ProgrammingError
from django.db.utils import OperationalError

def set_site(apps, schema_editor):
    try:
        site = Site.objects.create(id=2, name="CrowdBrew", domain="crowdbrew.local")
        site.save()
    except (ProgrammingError, OperationalError,):
        print "Unable to create CrowdBrew site"

def unset_site(apps, schema_editor):
    try:
        site = Site.objects.filter(id=2).delete()
    except (ProgrammingError, OperationalError,):
        print "Unable to delete CrowdBrew site"

class Migration(migrations.Migration):

    dependencies = [
        ('crowd_brew', '0003_auto_20150617_0811'),
    ]

    operations = [
        migrations.RunPython(set_site, unset_site),
    ]
