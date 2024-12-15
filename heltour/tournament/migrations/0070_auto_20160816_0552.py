# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 05:52


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0069_auto_20160816_0138"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerpairing",
            name="result",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1-0", "1-0"),
                    ("1/2-1/2", "\xbd-\xbd"),
                    ("0-1", "0-1"),
                    ("1X-0F", "1X-0F"),
                    ("1/2Z-1/2Z", "\xbdZ-\xbdZ"),
                    ("0F-1X", "0F-1X"),
                    ("0F-0F", "0F-0F"),
                ],
                max_length=16,
            ),
        ),
    ]
