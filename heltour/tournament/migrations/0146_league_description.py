# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-23 22:12


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0145_auto_20170211_1825"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
