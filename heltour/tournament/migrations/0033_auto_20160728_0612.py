# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 06:12


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0032_auto_20160728_0521"),
    ]

    operations = [
        migrations.RenameField(
            model_name="playerpairing",
            old_name="date_played",
            new_name="scheduled_time",
        ),
    ]
