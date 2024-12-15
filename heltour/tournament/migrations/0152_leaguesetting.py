# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-03 16:26


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0151_auto_20170322_2338"),
    ]

    operations = [
        migrations.CreateModel(
            name="LeagueSetting",
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
                    "limit_game_nominations_to_participants",
                    models.BooleanField(default=True),
                ),
                (
                    "league",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournament.League",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
