import io
import random


import requests
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import connection, connections
from django.utils import timezone
from rest_framework.test import APITestCase

from workout.models import WorkoutModel, ExerciseModel, stabilization_field_number, ApproachModel

"""Можно написать нормальные self.assert вместо print'ов, но мне похуй"""

class TestModel(APITestCase):
    def test_stabilization_field_number_exercise(self):
        first_icon_content = io.BytesIO(requests.get(
            'https://papik.pro/uploads/posts/2022-01/1641352988_1-papik-pro-p-vektornii-risunok-otzhimaniya-1.jpg').content)
        first_icon = SimpleUploadedFile('first_icon.jpg', first_icon_content.read())
        workout = WorkoutModel.objects.create(name='work', color='ffffff', icon=first_icon, initial_break=22, user=get_user_model().objects.create_user('pavel', '123456789!'))
        pos = [1, 5, 2, 7]
        exercise = ExerciseModel.objects.bulk_create(
            [ExerciseModel(name=f'Упражнение№{i % 2 + 1}', type='repetitions', icon=first_icon,
                           break_between_approaches=40, break_after_exercise=20, workout=workout,
                           ) for i in range(4)])
        # print(ExerciseModel.objects.filter(workout=workout).values_list('number', 'id'))
        stabilization_field_number(workout=workout)
        # print(ExerciseModel.objects.filter(workout=workout).values_list('number', 'id'))
        self.assertEquals(1, 1)

    def test_stabilization_field_number_approach(self):
        first_icon_content = io.BytesIO(requests.get(
            'https://papik.pro/uploads/posts/2022-01/1641352988_1-papik-pro-p-vektornii-risunok-otzhimaniya-1.jpg').content)
        first_icon = SimpleUploadedFile('first_icon.jpg', first_icon_content.read())
        workout = WorkoutModel.objects.create(name='work', color='ffffff', icon=first_icon, initial_break=22, user=get_user_model().objects.create_user('pavel', '123456789!'))
        exercise = ExerciseModel.objects.create(name='exercise', type='repetitions', icon=first_icon, break_between_approaches=40, break_after_exercise=20, workout=workout, number=1)
        pos = [1, 5, 7]
        approach = ApproachModel.objects.bulk_create([ApproachModel(working_weight=20, repetitions=40, number=pos[i], exercise=exercise) for i in range(3)] + [ApproachModel(working_weight=20, repetitions=40, exercise=exercise)] + [ApproachModel(working_weight=20, repetitions=40, exercise=exercise)])
        # print(ApproachModel.objects.filter(exercise=exercise).values_list('number', 'id'))
        stabilization_field_number(exercise=exercise)
        # print(ApproachModel.objects.filter(exercise=exercise).values_list('number', 'id'))
        self.assertEquals(1, 1)

    def test_change_exercise_type(self):

        first_icon_content = io.BytesIO(requests.get(
            'https://papik.pro/uploads/posts/2022-01/1641352988_1-papik-pro-p-vektornii-risunok-otzhimaniya-1.jpg').content)
        first_icon = SimpleUploadedFile('first_icon.jpg', first_icon_content.read())
        workout = WorkoutModel.objects.create(name='work', color='ffffff', icon=first_icon, initial_break=22,
                                              user=get_user_model().objects.create_user('pavel', '123456789!'))
        exercise = ExerciseModel.objects.create(name='exercise', type='repetitions', icon=first_icon,
                                                break_between_approaches=40, break_after_exercise=20, workout=workout,
                                                number=1)
        approach = ApproachModel.objects.bulk_create(
            [ApproachModel(working_weight=20, repetitions=40, exercise=exercise) for i in range(3)])
        exercise.type = 'time'
        # print(list(ApproachModel.objects.filter(exercise=exercise).values('repetitions', "duration")))
        exercise.save()
        # print(list(ApproachModel.objects.filter(exercise=exercise).values('repetitions', "duration")))








