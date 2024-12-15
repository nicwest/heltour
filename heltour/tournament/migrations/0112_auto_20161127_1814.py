# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-27 18:14


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0111_auto_20161109_0440"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scheduledevent",
            name="type",
            field=models.CharField(
                choices=[
                    ("notify_mods_unscheduled", "Notify mods of unscheduled games"),
                    ("notify_mods_no_result", "Notify mods of games without results"),
                    ("start_round_transition", "Start round transition"),
                ],
                max_length=255,
            ),
        ),
    ]
