# Generated by Django 4.2 on 2023-05-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_alter_exercisemodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisemodel',
            name='number',
            field=models.IntegerField(default=1000, null=True),
        ),
    ]