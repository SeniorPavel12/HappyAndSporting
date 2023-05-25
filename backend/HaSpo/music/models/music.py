import uuid

from django.db import models

from music.models.mixin import CheckUserModelMixin


class MusicModel(models.Model, CheckUserModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    title = models.CharField(max_length=200)

    content = models.FileField(upload_to='music/')

    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, related_name='music')

    playlist = models.ManyToManyField('music.PlaylistModel', related_name='used_music')

    path_to_user = 'user'


class PlaylistModel(models.Model, CheckUserModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    title = models.CharField(max_length=200)

    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, related_name='playlist')

    path_to_user = 'user'
