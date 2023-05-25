from workout.models import WorkoutModel, ExerciseModel, ApproachModel

"""_ является первым параметром тк в классах возникает проблема засовывания функции в свойства, а так мы получается создали методы"""


def get_all_workout_instances(_, user):
    return list(WorkoutModel.objects.filter(user=user))


def get_workout_instance(_, id):
    return WorkoutModel.objects.get(id=id)


def get_all_exercise_instances(_, user, link_field, link_id):
    return list(ExerciseModel.objects.filter(workout=link_id))


def get_exercise_instance(_, id):
    return ExerciseModel.objects.get(id=id)


def get_all_approach_instances(_, user, link_field, link_id):
    return list(ApproachModel.objects.filter(exercise=link_id))


def get_approach_instance(_, id):
    return ApproachModel.objects.get(id=id)


def get_not_free_workout_color(user):
    return list(WorkoutModel.objects.filter(user=user).values_list('color', flat=True))