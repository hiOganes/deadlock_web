# Generated by Django 5.1.3 on 2024-11-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_characters_sprint_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characters',
            name='spell1',
        ),
        migrations.RemoveField(
            model_name='characters',
            name='spell2',
        ),
        migrations.RemoveField(
            model_name='characters',
            name='spell3',
        ),
        migrations.RemoveField(
            model_name='characters',
            name='spellultimate',
        ),
    ]
