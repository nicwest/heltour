# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-18 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0183_playersetting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alternate",
            name="board_number",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                    (8, "8"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="alternateassignment",
            name="board_number",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                    (8, "8"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="alternatebucket",
            name="board_number",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                    (8, "8"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="alternatesearch",
            name="board_number",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                    (8, "8"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="board_number",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                    (8, "8"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="teamplayerpairing",
            name="board_number",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                    (8, "8"),
                ]
            ),
        ),
    ]
