# Generated by Django 5.0.4 on 2024-04-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Motorista",
            fields=[
                ("cod_motorista", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=50)),
                ("telefone", models.CharField(max_length=20, null=True)),
                ("num_cnh", models.CharField(max_length=20)),
            ],
        ),
    ]
