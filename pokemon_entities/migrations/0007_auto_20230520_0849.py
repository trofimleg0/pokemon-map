# Generated by Django 3.1.14 on 2023-05-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0006_auto_20230520_0848"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=20, verbose_name="Имя на английском"
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title_jp",
            field=models.CharField(
                blank=True, max_length=20, verbose_name="Имя на японском"
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title_ru",
            field=models.CharField(
                max_length=20, verbose_name="Имя на русском"
            ),
        ),
    ]
