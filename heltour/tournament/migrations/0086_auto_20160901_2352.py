# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 23:52


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0085_auto_20160901_2341"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="gameselection",
            unique_together=set([("season", "game_link")]),
        ),
    ]
