# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-01 23:39


from django.db import migrations
from reversion.models import Version
from heltour.tournament.models import Document


def forward(apps, schema_editor):
    for doc in Document.objects.all():
        version = (
            Version.objects.get_for_object(doc)
            .order_by("revision__date_created")
            .first()
        )
        if version:
            revision = version.revision
            creator = revision.user
            if creator:
                doc.owner = creator
                doc.save()


def reverse(apps, schema_editor):
    Document = apps.get_model("tournament", "Document")
    for doc in Document.objects.all():
        doc.owner = None
        doc.save()


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0172_auto_20171201_2339"),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
