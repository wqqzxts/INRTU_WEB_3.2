# Generated by Django 5.1.1 on 2024-10-07 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_alter_team_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
    ]
