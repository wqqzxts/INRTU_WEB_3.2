# Generated by Django 5.1.1 on 2024-10-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_alter_team_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='team_name',
        ),
    ]
