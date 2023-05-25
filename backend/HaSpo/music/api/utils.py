from HaSpo.constans import RequestError
from music.models import MusicModel


def add_music_to_playlist(playlist, musics):
    _data = []
    for id in musics:
        try:
            music = MusicModel.objects.get(id=id)
        except MusicModel.DoesNotExist:
            raise RequestError("Вы передали некорректный id музыки")
        music.playlist.add(playlist)
        _data.append(music)
    return _data
