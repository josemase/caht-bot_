# Generated by Django 4.2 on 2025-02-17 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_service', '0002_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='ChatResponse',
        ),
    ]
