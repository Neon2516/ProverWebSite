# Generated by Django 5.1.1 on 2024-10-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anketaApp", "0004_rename_bithdate_driver_bithdatedriver_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="numberAuto",
            field=models.CharField(max_length=12, verbose_name="Номер автомобиля"),
        ),
    ]