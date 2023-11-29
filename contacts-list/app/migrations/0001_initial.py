# Generated by Django 4.2.6 on 2023-11-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=30)),
                ("is_favorite", models.BooleanField()),
            ],
        ),
    ]