# Generated by Django 4.2 on 2023-05-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_alter_exercisemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approachmodel',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='approachmodel',
            name='number',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
