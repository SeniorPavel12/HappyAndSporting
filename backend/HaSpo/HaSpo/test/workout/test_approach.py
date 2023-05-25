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
from workout.api.viewsets.workout import WorkoutViewSet, ApproachViewSet
from workout.models import WorkoutModel, ApproachModel, ExerciseModel

from django.conf import settings


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestApproach(TestCase):
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
        view = ApproachViewSet.as_view({'post': 'custom_delete'})
        url = '/api/workout/approach/delete/'
        data = {"id": list(str(i) for i in ApproachModel.objects.all().values_list('id', flat=True))}
        request = self.factory.post(url, data)
        force_authenticate(request, user=self.user)
        response = view(request)
        re_data = data
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, re_data)
        self.assertEquals(len(ApproachModel.objects.all()), 0)

    def test_create(self):
        view = ApproachViewSet.as_view({'post': 'custom_create'})
        url = '/api/workout/approach/create/'
        exercise = ExerciseModel.objects.all()[0]
        data = {
            "working_weight": 232,
            'repetitions': 24,
            'exercise': str(exercise.id)

        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(ApproachModel.objects.filter(working_weight=232)), 1)
        self.assertEquals(data, {"id": ApproachModel.objects.filter(working_weight=232)[0].id})

    def test_get(self):
        url = '/api/workout/approach/get/'
        view = ApproachViewSet.as_view({'post': 'custom_get'})
        instance = ApproachModel.objects.all()[0]
        request = self.factory.post(url, data={"id": instance.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'id': str(instance.id), "working_weight": instance.working_weight, 'repetitions': instance.repetitions, "duration": instance.duration, "number": instance.number, "exercise": instance.exercise.id})

    def test_get_all(self):
        url = '/api/workout/approach/get_all/'
        view = ApproachViewSet.as_view({'post': 'custom_get_all'})
        instance = ExerciseModel.objects.all()[0]
        request = self.factory.post(url, data={"id": str(instance.id)})
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('approach', data.keys())
        self.assertEquals(len(data['approach']), len(ApproachModel.objects.filter(exercise=instance)))

    def test_update(self):
        url = '/api/workout/approach/update/'
        view = ApproachViewSet.as_view({'post': 'custom_update'})
        instance = ApproachModel.objects.all()[0]
        data = {
            "id": str(instance.id),
            "working_weight": 122,
            'repetitions': 131
        }
        request = self.factory.post(url, data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        data = dict(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(ApproachModel.objects.filter(working_weight=122)), 1)
        instance = ApproachModel.objects.filter(working_weight=122)[0]
        self.assertEquals(data, {'id': str(instance.id), "working_weight": instance.working_weight, 'repetitions': instance.repetitions, "duration": instance.duration, "number": instance.number, "exercise": instance.exercise.id})


    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT)
        super().tearDownClass()
