# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-28 20:49


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournament", "0164_logintoken_mail_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="peak_classical_rating",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
