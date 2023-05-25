import io
import json
import tempfile
import shutil
import uuid
from uuid import UUID

import requests
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.fields.files import ImageFieldFile
from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from workout.api.viewsets.workout import WorkoutViewSet
from workout.models import WorkoutModel, ApproachModel, ExerciseModel

from django.conf import settings


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestWorkout(TestCase):
    username = 'pavel'
    password = '123456789!'
    factory = APIRequestFactory()
    client = APIClient()

    def setUp(self):
        first_icon_content = io.BytesIO(requests.get(
            'https://papik.pro/uploads/posts/2022-01/1641352988_1-papik-pro-p-vektornii-risunok-otzhimaniya-1.jpg').content)
        second_icon_content = io.BytesIO(requests.get(
            'https://papik.pro/uploads/posts/2023-02/1677470701_papik-pro-p-legkaya-atletika-beg-risunki-11.jpg').content)
        self.first_icon, self.second_icon = first_icon, second_icon = SimpleUploadedFile('first_icon.jpg',
                                                                                         first_icon_content.read()), SimpleUploadedFile(
            'second_icon.jpg', second_icon_content.read())
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)
        workout = WorkoutModel.objects.bulk_create(
            [WorkoutModel(name=f'Тренировка№{i + 1}', color=f'{i} {i + 2} {i + 3}', icon=first_icon, initial_break=50,
                          user=self.user) for i in range(2)])
        exercise = ExerciseModel.objects.bulk_create(
            [ExerciseModel(name=f'Упражнение№{i % 2 + 1}', type='repetitions', icon=second_icon,
                           break_between_approaches=40, break_after_exercise=20, workout=workout[i // 2],
                           number=i % 2 + 1) for i in range(4)])
        ApproachModel.objects.bulk_create(
            [ApproachModel(working_weight=10, repetitions=30, number=i % 2 + 1, exercise=exercise[i // 2]) for i in
             range(8)])

    def test_delete(self):
        view = WorkoutViewSet.as_view({'post': 'custom_delete'})
        url = '/api/workout/workout/delete/'
        data = {"id": list(str(i) for i in WorkoutModel.objects.all().values_list('id', flat=True))}
        request = self.factory.post(url, data)
        force_authenticate(request, user=self.user)
        response = view(request)
        re_data = data
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, re_data)
        self.assertEquals(len(WorkoutModel.objects.all()), 0)

    def test_create(self):
        view = WorkoutViewSet.as_view({'post': 'custom_create'})
        url = '/api/workout/workout/create/'
        workout = WorkoutModel.objects.all()[0]
        with self.first_icon.open() as f:
            data = {
                "name": "CreateWorkout",
                "icon": f,
                "color": 'ffffff',
                'initial_break': 21
            }
            request = self.factory.post(url, data=data)
            force_authenticate(request, user=self.user)
            response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(WorkoutModel.objects.filter(name='CreateWorkout')), 1)
        self.assertEquals(data, {"id": WorkoutModel.objects.filter(name='CreateWorkout')[0].id})

    def test_get(self):
        url = '/api/workout/workout/get/'
        view = WorkoutViewSet.as_view({'post': 'custom_get'})
        instance = WorkoutModel.objects.all()[0]
        request = self.factory.post(url, data={"id": instance.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('icon', data.keys())
        data.pop('icon')
        self.assertEquals(data, {"id": str(instance.id), "name": instance.name, "color": instance.color,
                                 "initial_break": instance.initial_break, 'playlist': instance.playlist})

    def test_get_all(self):
        url = '/api/workout/workout/get_all/'
        view = WorkoutViewSet.as_view({'post': 'custom_get_all'})
        request = self.factory.post(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('workout', data.keys())
        self.assertEquals(len(data['workout']), len(WorkoutModel.objects.all()))

    def test_update(self):
        url = '/api/workout/exercise/update/'
        view = WorkoutViewSet.as_view({'post': 'custom_update'})
        instance = WorkoutModel.objects.all()[0]
        with self.first_icon.open() as f:
            data = {
                "id": str(instance.id),
                "name": "UpdateWorkout",
                "icon": f,
                "color": 'ffffff',
                'initial_break': 21
            }
            request = self.factory.post(url, data=data)
            force_authenticate(request, user=self.user)
            response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(WorkoutModel.objects.filter(name='UpdateWorkout')), 1)
        instance = WorkoutModel.objects.filter(name='UpdateWorkout')[0]
        self.assertIn('icon', data.keys())
        data.pop('icon')
        self.assertEquals(data, {'id': str(instance.id), "name": instance.name, "color": instance.color,
                                 "initial_break": instance.initial_break, 'playlist': instance.playlist})

    def test_invalid_user(self):
        test_user = get_user_model().objects.create_user(username='test', password='123456789!')
        wor = WorkoutModel.objects.create(name='w', color='121212', icon=self.first_icon, initial_break=23,
                                          user=test_user)
        url = '/api/workout/workout/get/'
        view = WorkoutViewSet.as_view({'post': 'custom_get'})
        instance = wor
        request = self.factory.post(url, data={"id": instance.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(data, {'detail': (
        'Вы можете взаимодействовать только с теми объекты которые принадлежат вашему текущему пользователю',)})

    def test_get_not_free_workout_color(self):
        url = '/api/workout/workout/get/'
        view = WorkoutViewSet.as_view({'post': 'get_not_free_workout_color'})
        request = self.factory.post(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data,
                          {"color": list(WorkoutModel.objects.filter(user=self.user).values_list('color', flat=True))})

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT)
        super().tearDownClass()
