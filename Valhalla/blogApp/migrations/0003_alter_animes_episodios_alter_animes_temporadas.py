# Generated by Django 4.1.3 on 2022-12-01 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_animes_episodios_alter_animes_temporadas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animes',
            name='episodios',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='animes',
            name='temporadas',
            field=models.IntegerField(blank=True),
        ),
    ]
