# Generated by Django 4.2.3 on 2023-07-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarModel",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="FuelTypeModel",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="bookmodel",
            name="authors",
        ),
        migrations.DeleteModel(
            name="AuthorModel",
        ),
        migrations.DeleteModel(
            name="BookModel",
        ),
        migrations.AddField(
            model_name="carmodel",
            name="fueltype",
            field=models.ManyToManyField(to="app.fueltypemodel"),
        ),
    ]
