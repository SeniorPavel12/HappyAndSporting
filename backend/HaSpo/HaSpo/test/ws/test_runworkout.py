import asyncio
import io

import pytest
from aioconsole import aprint

import requests
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from channels.routing import URLRouter
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import connection, connections
from django.urls import path
from rest_framework.parsers import JSONParser
from rest_framework.test import APITestCase, APIClient
from channels.testing import HttpCommunicator, WebsocketCommunicator, ChannelsLiveServerTestCase
from django.test import Client, TestCase

from workout.models import WorkoutModel, ExerciseModel, ApproachModel
from workout.wb.consumer import RunWorkoutConsumer


@pytest.mark.asyncio
@pytest.mark.django_db(True)
@pytest.mark.django_db(transaction=True)
async def test_workout():
    try:
        workout = await custom_setup()
        print(await create_plan_workout(workout), len(await create_plan_workout(workout)))
        communicator = WebsocketCommunicator(RunWorkoutConsumer.as_asgi(), "ws/run_workout/")
        await communicator.connect()
        await communicator.send_to(text_data=f'''{{"type": "SW", "workout": "{str(workout.id)}"}}''')
        response = await communicator.receive_from()
        print(response)
        await communicator.send_to(text_data=f'''{{"type": "NT"}}''')
        response = await communicator.receive_from()
        print(response)
        await communicator.send_to(text_data=f'''{{"type": "NT"}}''')
        response = await communicator.receive_from()
        print(response)
        await communicator.send_to(text_data=f'''{{"type": "NT"}}''')
        response = await communicator.receive_from()
        print(response)
        await communicator.send_to(text_data=f'''{{"type": "NT"}}''')
        response = await communicator.receive_from()
        print(response)
        await communicator.disconnect()
    finally:
        # Close the database connection at the end of the test

        await database_sync_to_async(connections.close_all)()


@database_sync_to_async
def custom_setup():
    first_icon_content = io.BytesIO(requests.get(
        'https://papik.pro/uploads/posts/2022-01/1641352988_1-papik-pro-p-vektornii-risunok-otzhimaniya-1.jpg').content)
    second_icon_content = io.BytesIO(requests.get(
        'https://papik.pro/uploads/posts/2023-02/1677470701_papik-pro-p-legkaya-atletika-beg-risunki-11.jpg').content)
    first_icon, second_icon = SimpleUploadedFile('first_icon.jpg',
                                                 first_icon_content.read()), SimpleUploadedFile(
        'second_icon.jpg', second_icon_content.read())
    user = get_user_model().objects.create_user(username='pavel121212', password='123456789!')
    workout = WorkoutModel.objects.bulk_create(
        [WorkoutModel(name=f'Тренировка№{i + 1}', color=f'{i} {i + 2} {i + 3}', icon=first_icon, initial_break=50,
                      user=user) for i in range(2)])
    exercise = ExerciseModel.objects.bulk_create(
        [ExerciseModel(name=f'Упражнение№{i % 2 + 1}', type='repetitions', icon=second_icon,
                       break_between_approaches=40, break_after_exercise=20, workout=workout[i // 2],
                       number=i % 2 + 1) for i in range(4)])
    ApproachModel.objects.bulk_create(
        [ApproachModel(working_weight=10, repetitions=30, number=i % 2 + 1, exercise=exercise[i // 2]) for i in
         range(8)])
    return WorkoutModel.objects.all()[0]

@database_sync_to_async
def create_plan_workout(workout):
    main = []
    main.append(['break', {"time": workout.initial_break}])
    exercises = workout.exercises.all()
    for exe in exercises:
        ind_exe = list(exercises).index(exe)
        type = exe.type
        break_between_approaches = exe.break_between_approaches
        approaches = exe.approaches.all()
        for app in approaches:
            ind_app = list(approaches).index(app)
            if type == 'repetitions':
                main.append(["approach", {"repetitions": app.repetitions, "working_weight": app.working_weight}])
            else:
                main.append(["approach", {"repetitions": app.repetitions, "working_weight": app.working_weight}])
            if ind_app == len(approaches) - 1:
                break
            main.append(["break", {"time": break_between_approaches}])
        if ind_exe == len(exercises) - 1:
            break
        break_after_exercise = exe.break_after_exercise
        main.append(["break", {"time": break_after_exercise}])
    return main
