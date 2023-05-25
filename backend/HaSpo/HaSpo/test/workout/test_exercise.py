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

from workout.api.viewsets import ExerciseViewSet
from workout.api.viewsets.workout import WorkoutViewSet
from workout.models import WorkoutModel, ApproachModel, ExerciseModel

from django.conf import settings

# !!!
# Написать тесты проверяющие изменения типа exercise


















@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestExercise(TestCase):
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
        view = ExerciseViewSet.as_view({'post': 'custom_delete'})
        url = '/api/workout/exercise/delete/'
        data = {"id": list(str(i) for i in ExerciseModel.objects.all().values_list('id', flat=True))}
        request = self.factory.post(url, data)
        force_authenticate(request, user=self.user)
        response = view(request)
        re_data = data
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, re_data)
        self.assertEquals(len(ExerciseModel.objects.all()), 0)

    def test_create(self):
        view = ExerciseViewSet.as_view({'post': 'custom_create'})
        url = '/api/workout/exersice/create/'
        workout = WorkoutModel.objects.all()[0]
        with self.first_icon.open() as f:
            data = {
                "name": "FirstExercise",
                "icon": f,
                "type": 'time',
                'break_between_approaches': 131,
                'break_after_exercise': 24,
                'number': 1,
                'workout': str(workout.id)

            }
            request = self.factory.post(url, data=data)
            force_authenticate(request, user=self.user)
            response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(ExerciseModel.objects.filter(name='FirstExercise')), 1)
        self.assertEquals(data, {"id": ExerciseModel.objects.filter(name='FirstExercise')[0].id})

    def test_get(self):
        url = '/api/workout/exercise/get/'
        view = ExerciseViewSet.as_view({'post': 'custom_get'})
        instance = ExerciseModel.objects.all()[0]
        request = self.factory.post(url, data={"id": instance.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('icon', data.keys())
        data.pop('icon')
        self.assertEquals(data, {"id": str(instance.id), "name": instance.name, 'type': instance.type, "break_between_approaches": instance.break_between_approaches, "break_after_exercise": instance.break_after_exercise, "number": instance.number, "workout": instance.workout.id})

    def test_get_all(self):
        url = '/api/workout/exercise/get_all/'
        view = ExerciseViewSet.as_view({'post': 'custom_get_all'})
        instance = WorkoutModel.objects.all()[0]
        request = self.factory.post(url, data={"id": str(instance.id)})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('exercise', data.keys())
        self.assertEquals(len(data['exercise']), len(ExerciseModel.objects.filter(workout=instance)))

    def test_update(self):
        url = '/api/workout/exercise/update/'
        view = ExerciseViewSet.as_view({'post': 'custom_update'})
        instance = ExerciseModel.objects.all()[0]
        with self.first_icon.open() as f:
            data = {
                "id": str(instance.id),
                "name": "UpdateExercise",
                "icon": f,
                "type": 'time',
                'break_between_approaches': 131,
                'break_after_exercise': 24,
                'number': 1
            }
            request = self.factory.post(url, data=data)
            force_authenticate(request, user=self.user)
            response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(ExerciseModel.objects.filter(name='UpdateExercise')), 1)
        instance = ExerciseModel.objects.filter(name='UpdateExercise')[0]
        self.assertIn('icon', data.keys())
        data.pop('icon')
        self.assertEquals(data, {"id": str(instance.id), "name": instance.name, 'type': instance.type, "break_between_approaches": instance.break_between_approaches, "break_after_exercise": instance.break_after_exercise, "number": instance.number, "workout": instance.workout.id})


    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT)
        super().tearDownClass()
