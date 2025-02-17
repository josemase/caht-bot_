# Generated by Django 4.2 on 2025-02-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_service', '0003_rename_response_chatresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalabrasClave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.TextField()),
                ('palabras', models.JSONField()),
            ],
            options={
                'db_table': 'palabras_clave',
            },
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.TextField()),
                ('tipo', models.TextField()),
                ('marca', models.TextField()),
                ('modelo', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('specs', models.JSONField()),
            ],
            options={
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='respuestas_generales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField()),
                ('respuesta', models.TextField()),
            ],
            options={
                'db_table': 'respuestas_generales',
            },
        ),
    ]
