# Generated by Django 4.2.1 on 2023-05-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_remove_musicmodel_playlist_musicmodel_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicmodel',
            name='playlist',
            field=models.ManyToManyField(related_name='used_music', to='music.playlistmodel'),
        ),
    ]
