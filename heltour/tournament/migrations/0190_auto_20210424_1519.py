# Generated by Django 2.2.13 on 2021-04-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0189_auto_20210221_0424"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="date_first_agreed_to_tos",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="player",
            name="date_last_agreed_to_tos",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="agreed_to_tos",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
