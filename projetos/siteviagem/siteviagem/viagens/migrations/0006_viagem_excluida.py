# Generated by Django 5.1.4 on 2025-01-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagens', '0005_viagem_nome_motorista_alter_viagem_destino'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='excluida',
            field=models.BooleanField(default=False),
        ),
    ]
