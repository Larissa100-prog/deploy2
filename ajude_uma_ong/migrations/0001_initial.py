# Generated by Django 5.1.3 on 2024-11-30 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ONG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pauta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('prazo', models.DateField(blank=True, null=True)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pautas', to='ajude_uma_ong.ong')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=255)),
                ('email_pessoa', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
                ('pauta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ajudas', to='ajude_uma_ong.pauta')),
            ],
        ),
    ]
