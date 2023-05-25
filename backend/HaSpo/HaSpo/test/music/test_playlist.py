import shutil
from io import BytesIO

import requests
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.conf import settings
from django.test import override_settings

from music.api.viewsets.viewset import PlaylistViewSet
from music.models import PlaylistModel, MusicModel



@override_settings(MEDIA_ROOT='/test_media/')
class TestMusic(APITestCase):
    factory = APIRequestFactory()

    def setUp(self):
        self.user = get_user_model().objects.create_user('pavel', '123456789!')
        PlaylistModel.objects.create(title='first_playlist', user=self.user)

    def test_get_all(self):
        url = '/music/playlist/get_all/'
        view = PlaylistViewSet.as_view({'post': 'custom_get_all'})
        instance = PlaylistModel.objects.all()[0]
        request = self.factory.post(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data,
                          {"playlist": [{'id': str(instance.id), 'title': instance.title}]})

    def test_get(self):
        url = '/music/playlist/get/'
        view = PlaylistViewSet.as_view({'post': 'custom_get'})
        instance = PlaylistModel.objects.all()[0]
        request = self.factory.post(url, data={"id": instance.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {"id": str(instance.id), "title": instance.title})

    def test_create(self):
        url = '/music/playlist/create/'
        view = PlaylistViewSet.as_view({'post': 'custom_create'})
        data = {
            "title": "create_playlist"
        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(PlaylistModel.objects.filter(title='create_playlist')), 1)
        self.assertEquals(data, {"id": PlaylistModel.objects.filter(title='create_playlist')[0].id})

    def test_update(self):
        url = '/music/playlist/update/'
        view = PlaylistViewSet.as_view({'post': 'custom_update'})
        instance = PlaylistModel.objects.all()[0]
        data = {
            "id": str(instance.id),
            "title": "update_playlist",
        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(PlaylistModel.objects.filter(title='update_playlist')), 1)
        instance = PlaylistModel.objects.filter(title='update_playlist')[0]
        self.assertEquals(data, {"id": str(instance.id), "title": instance.title})

    def test_delete(self):
        url = '/music/playlist/delete/'
        view = PlaylistViewSet.as_view({'post': 'custom_delete'})
        instance = PlaylistModel.objects.all()[0]
        data = {
            "id": [str(instance.id)]
        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        re_data = data
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(PlaylistModel.objects.all()), 0)
        self.assertEquals(data, re_data)

    def test_add_many_music_to_playlist(self):
        url = '/music/playlist/add_many_music_to_playlist/'
        view = PlaylistViewSet.as_view({'post': 'add_many_music_to_playlist'})
        playlist = PlaylistModel.objects.all()[0]
        self.first_audio = SimpleUploadedFile('first_audio.mp3', BytesIO(requests.get(
            'https://dl4s4.hitmo.top/aHR0cDovL2YubXAzcG9pc2submV0L21wMy8wMDUvMTI0LzM5MC81MTI0MzkwLm1wMz90aXRsZT1UaGUrQm95eistK05vbHphKyUyOGhpdG1vLnRvcCUyOS5tcDM=').content).read())
        music = [MusicModel.objects.create(title='Название 1', content=self.first_audio, user=self.user), MusicModel.objects.create(title='Название 2', content=self.first_audio, user=self.user)]
        data = {
            "playlist": str(playlist.id),
            'music': [str(i.id) for i in music]
        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'music': [str(i.id) for i in music]})
        self.assertTrue(all(map(lambda x: True if playlist in x.playlist.all() else False, MusicModel.objects.all())))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT)
        super().tearDownClass()