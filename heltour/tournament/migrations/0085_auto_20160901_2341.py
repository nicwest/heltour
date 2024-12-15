# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 23:41


import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0084_gamenomination_pairing"),
    ]

    operations = [
        migrations.CreateModel(
            name="GameSelection",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "game_link",
                    models.URLField(
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile(
                                    "^(https?://)?([a-z]+\\.)?lichess\\.org/([A-Za-z0-9]{8})([A-Za-z0-9]{4})?([/#\\?].*)?$"
                                )
                            )
                        ]
                    ),
                ),
                (
                    "pairing",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tournament.PlayerPairing",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterModelOptions(
            name="season",
            options={
                "permissions": (
                    ("manage_players", "Can manage players"),
                    ("review_nominated_games", "Can review nominated games"),
                )
            },
        ),
        migrations.AddField(
            model_name="gameselection",
            name="season",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tournament.Season"
            ),
        ),
    ]
