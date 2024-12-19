# Generated by Django 5.1.1 on 2024-12-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0017_contenttype_user_position_user_skills_user_team_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]