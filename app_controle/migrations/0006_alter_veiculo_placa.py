# Generated by Django 5.0.4 on 2024-04-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_controle", "0005_alter_motorista_num_cnh"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="placa",
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
