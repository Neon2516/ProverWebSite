# Generated by Django 5.1.1 on 2024-10-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                (
                    "numberAuto",
                    models.CharField(max_length=9, verbose_name="Номер автомобиля"),
                ),
                ("firmAuto", models.CharField(max_length=50, verbose_name="Марка")),
                ("modelAuto", models.CharField(max_length=50, verbose_name="Модель")),
                ("dateCreate", models.DateField(verbose_name="Год выпуска")),
                (
                    "powerEngine",
                    models.CharField(max_length=50, verbose_name="Мощность двигателя"),
                ),
                (
                    "numberSTS",
                    models.CharField(max_length=10, verbose_name="Серия и номер СТС"),
                ),
                ("dateGiveDoc", models.DateField(verbose_name="Дата выдачи документа")),
                (
                    "numberVIN",
                    models.CharField(max_length=50, verbose_name="VIN номер"),
                ),
            ],
        ),
    ]
