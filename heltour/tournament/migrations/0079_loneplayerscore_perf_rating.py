# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 21:44


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0078_auto_20160820_0049"),
    ]

    operations = [
        migrations.AddField(
            model_name="loneplayerscore",
            name="perf_rating",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
