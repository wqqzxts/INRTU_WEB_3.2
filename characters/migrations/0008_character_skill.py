# Generated by Django 5.1.1 on 2024-10-08 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.skills'),
        ),
    ]
