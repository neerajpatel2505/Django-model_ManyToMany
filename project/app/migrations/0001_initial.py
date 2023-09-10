# Generated by Django 4.2.3 on 2023-07-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthorModel",
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
                ("name", models.CharField(max_length=100, verbose_name="Aut_Name")),
                ("desc", models.TextField(max_length=300, verbose_name="Aut_Desc")),
                ("city", models.CharField(max_length=100, verbose_name="Aut_city")),
            ],
        ),
        migrations.CreateModel(
            name="BookModel",
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
                ("title", models.CharField(max_length=100, verbose_name="Book_title")),
                ("desc", models.TextField(max_length=300, verbose_name="Book_desc")),
                (
                    "authors",
                    models.ManyToManyField(
                        to="app.authormodel", verbose_name="Book_auth"
                    ),
                ),
            ],
        ),
    ]
