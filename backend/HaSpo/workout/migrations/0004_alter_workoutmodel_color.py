# Generated by Django 4.2 on 2023-04-28 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_alter_approachmodel_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutmodel',
            name='color',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.RegexValidator(message='Строка должна соответствовать значению цвета в HEX', regex='[0-9A-Fa-f]{6}')]),
        ),
    ]