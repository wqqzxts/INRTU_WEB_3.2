# Generated by Django 5.1.1 on 2024-12-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_skills_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='picture',
            field=models.ImageField(null=True, upload_to='characters', verbose_name='Изображение'),
        ),
    ]
