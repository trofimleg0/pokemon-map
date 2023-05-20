# Generated by Django 3.1.14 on 2023-05-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title_ru", models.CharField(max_length=20)),
                ("title_en", models.CharField(blank=True, max_length=20)),
                ("title_jp", models.CharField(blank=True, max_length=20)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="PokemonEntity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latitude", models.FloatField(max_length=50)),
                ("longitude", models.FloatField(max_length=50)),
                ("appeared_at", models.DateTimeField(blank=True)),
                ("disappeared_at", models.DateTimeField(blank=True)),
                ("level", models.IntegerField(blank=True)),
                ("health", models.IntegerField(blank=True)),
                ("strength", models.IntegerField(blank=True)),
                ("defence", models.IntegerField(blank=True)),
                ("stamina", models.IntegerField(blank=True)),
                (
                    "pokemon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pokemon_entities.pokemon",
                    ),
                ),
            ],
        ),
    ]