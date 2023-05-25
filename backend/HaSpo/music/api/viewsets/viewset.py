from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from music.api.service import get_music_instance, get_all_music_instances, get_playlist_instance, \
    get_all_playlist_instances, get_playlist
from music.api.serializers import *
from music.api.utils import add_music_to_playlist
from music.api.viewsets.mixin import *
from music.models import PlaylistModel


class MusicViewSet(ViewSet, GetViewSetMixin, GetAllViewSetMixin, CreateViewSetMixin, UpdateViewSetMixin,
                   DeleteViewSetMixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    basename = 'music'

    get_instance = get_music_instance
    get_all_instances = get_all_music_instances

    get_serializer = GetMusicSerializer
    get_all_serializer = GetAllMusicSerializer
    update_serializer = UpdateMusicSerializer
    create_serializer = CreateMusicSerializer
    delete_serializer = DeleteMusicSerializer

    readable_name = 'music'
    model = MusicModel
    link_field = None


"""Добавить Action для для добавления произведений в плейлист"""


class PlaylistViewSet(ViewSet, GetViewSetMixin, GetAllViewSetMixin, CreateViewSetMixin, UpdateViewSetMixin,
                      DeleteViewSetMixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    basename = 'playlist'

    get_instance = get_playlist_instance
    get_all_instances = get_all_playlist_instances

    get_serializer = GetPlaylistSerializer
    get_all_serializer = GetAllPlaylistSerializer
    update_serializer = UpdatePlaylistSerializer
    create_serializer = CreatePlaylistSerializer
    delete_serializer = DeletePlaylistSerializer

    readable_name = 'playlist'
    model = PlaylistModel
    link_field = None

    @action(detail=False, methods=['post'], url_path='add_many_music_to_playlist', renderer_classes=[JSONRenderer])
    @check_exception
    @check_validate_user
    def add_many_music_to_playlist(self, request):
        """Принимает id плейлиста и id песен которые нужно добавить({"playlist": id, "music": [id, id, id...]}), возвращает id добавленной музыки"""
        _data = []
        data = dict(request.data)
        playlist_id = data['playlist'][0]
        playlist = get_playlist(playlist_id)
        _data.append(playlist)
        _data.extend(add_music_to_playlist(playlist, data['music']))
        response = {"music": data['music']}
        response.update({"_control_data": _data})
        return Response(response)




