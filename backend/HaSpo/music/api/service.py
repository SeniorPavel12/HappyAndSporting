from HaSpo.constans import RequestError
from music.models import MusicModel, PlaylistModel

"""_ является первым параметром тк в классах возникает проблема засовывания функции в свойства, а так мы получается создали методы"""
def get_all_music_instances(_, user):
    return list(MusicModel.objects.filter(user=user))


def get_music_instance(_, id):
    return MusicModel.objects.get(id=id)


def get_all_playlist_instances(_, user):
    return list(PlaylistModel.objects.filter(user=user))


def get_playlist_instance(_, id):
    return PlaylistModel.objects.get(id=id)


def get_playlist(id):
    try:
        playlist = PlaylistModel.objects.get(id=id)
    except PlaylistModel.DoesNotExist:
        raise RequestError("Вы передали некорректный id плейлиста")
    return playlist

