# Generated by Django 5.0.4 on 2024-04-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_controle", "0004_alter_controle_km_percorrido_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="motorista",
            name="num_cnh",
            field=models.CharField(
                max_length=20, unique=True, verbose_name="N° da CNH"
            ),
        ),
    ]
