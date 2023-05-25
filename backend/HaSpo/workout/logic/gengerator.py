from channels.db import database_sync_to_async

from workout.logic.events import RequestEvent, ResponseEvent
from workout.models import WorkoutModel, ExerciseModel


async def main_handle():
    print('gen1handle')
    event = yield
    assert isinstance(event, RequestEvent)
    assert event.workout is not None
    gen = workout_generator(event.workout)
    while True:
        print("event!!!", event.type)
        if event.type == 'NT':
            try:
                res_eve = await gen.__anext__()
            except StopAsyncIteration:
                event = yield ResponseEvent("end", {'all_approach_completed': True})
                continue
            try:
                if res_eve.type == 'approach':
                    res_eve = [res_eve, await gen.__anext__()]
                event = yield res_eve
            except StopAsyncIteration:
                event = yield ResponseEvent(res_eve.type, res_eve.data, other_data={"last_approach": True})
        elif event.type == 'EW':
            event = yield ResponseEvent("end", {'all_approach_completed': False})
        elif event.type == 'SW':
            first_break = await gen.__anext__()
            first_app = await gen.__anext__()
            event = yield [ResponseEvent(first_break.type, first_break.data,
                                         other_data={"count_all_approach": await get_all_approach(event.workout)}),
                           first_app]
        else:
            raise KeyError("Вы еблан")


@database_sync_to_async
def get_all_approach(workout):
    res = 0
    for e in ExerciseModel.objects.filter(workout=workout):
        res += e.approaches.all().count()
    return res


async def workout_generator(workout):
    yield ResponseEvent('break', {"time": workout.initial_break})
    exercises = workout.exercises.all()
    async for exe in exercises:
        ind_exe = list(exercises).index(exe)
        type = exe.type
        break_between_approaches = exe.break_between_approaches
        print(2)
        other_data_app = {"count_exercise": await exe.approaches.acount(), "image_exercise": exe.icon,
                          "name_exercise": exe.name}
        approaches = exe.approaches.all()
        async for app in approaches:
            ind_app = list(approaches).index(app)
            other_data = None
            if ind_app == 0:
                other_data = other_data_app
            if type == 'repetitions':
                yield ResponseEvent("approach", {"repetitions": app.repetitions, "working_weight": app.working_weight},
                                    other_data)
            else:
                yield ResponseEvent("approach", {"repetitions": app.repetitions, "working_weight": app.working_weight},
                                    other_data)
            if ind_app == len(approaches) - 1:
                break
            yield ResponseEvent("break", {"time": break_between_approaches})
        if ind_exe == len(exercises) - 1:
            break
        break_after_exercise = exe.break_after_exercise
        yield ResponseEvent("break", {"time": break_after_exercise})
