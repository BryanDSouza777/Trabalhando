# Generated by Django 4.1.3 on 2022-12-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_alter_animes_episodios_alter_animes_temporadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='animes',
            name='sinopse2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='animes',
            name='sinopse3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='especificações2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='especificações3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jogos',
            name='descrição2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jogos',
            name='descrição3',
            field=models.TextField(blank=True),
        ),
    ]