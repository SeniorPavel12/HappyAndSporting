# Generated by Django 4.2 on 2023-04-25 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approachmodel',
            name='break_after_approach',
        ),
    ]
