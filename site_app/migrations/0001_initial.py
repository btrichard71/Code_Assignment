# Generated by Django 4.1 on 2022-08-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Results",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("avg_max_temperature", models.FloatField()),
                ("avg_min_temperature", models.FloatField()),
                ("total_precipitation", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("max_temperature", models.FloatField()),
                ("min_temperature", models.FloatField()),
                ("precipitation", models.FloatField()),
                ("station_id", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Yield",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_corn", models.IntegerField()),
                ("year", models.IntegerField()),
            ],
        ),
    ]
