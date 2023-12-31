# Generated by Django 4.2.3 on 2023-09-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="posts",
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
                ("headline", models.CharField(max_length=50)),
                ("sub_headline", models.CharField(max_length=250)),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="")),
                ("body", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="tags",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
    ]
