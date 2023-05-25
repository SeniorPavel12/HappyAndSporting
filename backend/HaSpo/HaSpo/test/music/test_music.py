import shutil
import tempfile
from collections import OrderedDict
from io import BytesIO
import requests

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.test import override_settings
from django.conf import settings

from music.api.viewsets.viewset import MusicViewSet
from music.models import MusicModel, PlaylistModel

"""
Написать тест на изменения плейлиста
Работу с объектами не принадлежащие данному user
"""
@override_settings(MEDIA_ROOT='/test_media/')
class TestMusic(APITestCase):
    factory = APIRequestFactory()

    def setUp(self):
        self.first_audio = SimpleUploadedFile('first_audio.mp3', BytesIO(requests.get(
            'https://dl4s4.hitmo.top/aHR0cDovL2YubXAzcG9pc2submV0L21wMy8wMDUvMTI0LzM5MC81MTI0MzkwLm1wMz90aXRsZT1UaGUrQm95eistK05vbHphKyUyOGhpdG1vLnRvcCUyOS5tcDM=').content).read())
        self.second_audio = SimpleUploadedFile('second_audio.mp3', BytesIO(requests.get(
            'https://dl4s4.hitmo.top/aHR0cDovL2YubXAzcG9pc2submV0L21wMy8wMDUvMTI0LzM5Mi81MTI0MzkyLm1wMz90aXRsZT0lRDAlOTAlRDAlQkQlRDElODIlRDAlQkUlRDAlQkQrJUQwJTlEJUQwJUI1JUQwJUIxJUQwJUJFKy0rJUQwJUExJUQwJUJCJUQwJUJFJUQwJUIyJUQwJUIwKyVEMCVCMSVEMSU4MyVEMCVCNCVEMSU4MiVEMCVCRSslRDAlQkYlRDElODMlRDAlQkIlRDAlQjgrJTI4aGl0bW8udG9wJTI5Lm1wMw==').content).read())
        self.user = get_user_model().objects.create_user('pavel', '123456789!')
        m = MusicModel.objects.create(title='first_music', content=self.first_audio, user=self.user)

    def test_get_all(self):
        url = '/music/music/get_all/'
        view = MusicViewSet.as_view({'post': 'custom_get_all'})
        instance = MusicModel.objects.all()[0]
        request = self.factory.post(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data,
                          {"music": [OrderedDict({'id': str(instance.id), 'title': instance.title, 'playlist': [i.id for i in instance.playlist.all()]})]})

    def test_get(self):
        url = '/music/music/get/'
        view = MusicViewSet.as_view({'post': 'custom_get'})
        instance = MusicModel.objects.all()[0]
        request = self.factory.post(url, data={"id": instance.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('content', data.keys())
        data.pop('content')
        self.assertEquals(data, {"id": str(instance.id), "title": instance.title, 'playlist': [i.id for i in instance.playlist.all()]})

    def test_create(self):
        url = '/music/music/create/'
        view = MusicViewSet.as_view({'post': 'custom_create'})
        with self.first_audio.open() as f:
            data = {
                "title": "create_music",
                "content": f
            }
            request = self.factory.post(url, data=data)
            force_authenticate(request, user=self.user)
            response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(MusicModel.objects.filter(title='create_music')), 1)
        self.assertEquals(data, {"id": MusicModel.objects.filter(title='create_music')[0].id})

    def test_update(self):
        url = '/music/music/update/'
        view = MusicViewSet.as_view({'post': 'custom_update'})
        instance = MusicModel.objects.all()[0]
        playlist = PlaylistModel.objects.create(title='playlist', user=self.user)
        with self.second_audio.open() as f:
            data = {
                "id": str(instance.id),
                "title": "update_music",
                "content": f,
                "playlist": [str(playlist.id)]
            }
            request = self.factory.post(url, data=data)
            force_authenticate(request, user=self.user)
            response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(MusicModel.objects.filter(title='update_music')), 1)
        instance = MusicModel.objects.filter(title='update_music')[0]
        self.assertIn('content', data.keys())
        data.pop('content')
        self.assertEquals(data, {"id": str(instance.id), "title": instance.title, 'playlist': [i.id for i in instance.playlist.all()]})

    def test_delete(self):
        url = '/music/music/delete/'
        view = MusicViewSet.as_view({'post': 'custom_delete'})
        instance = MusicModel.objects.all()[0]
        data = {
            "id": [str(instance.id)]
        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        re_data = data
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(MusicModel.objects.all()), 0)
        self.assertEquals(data, re_data)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT)
        super().tearDownClass()