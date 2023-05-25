import uuid

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from music.models import CheckUserModelMixin


class WorkoutModel(models.Model, CheckUserModelMixin):
    color_validator = RegexValidator(regex=r"[0-9A-Fa-f]{6}",
                                     message='Строка должна соответствовать значению цвета в HEX')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.CharField(unique=True, max_length=50)

    color = models.CharField(max_length=6, validators=[color_validator, ])

    icon = models.ImageField(upload_to='workout/icon/')

    initial_break = models.IntegerField()

    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, related_name='workout')

    playlist = models.ForeignKey('music.PlaylistModel', on_delete=models.SET_NULL, null=True,
                                 related_name='used_workout')
    path_to_user = 'user'

    class Meta:
        db_table = 'workout__workout'
        unique_together = ['color', 'user']


class ExerciseModel(models.Model, CheckUserModelMixin):
    class TypeChoice(models.TextChoices):
        time = 'time', _('Time')
        repetitions = 'repetitions', _('Repetitions')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.CharField(max_length=200)

    type = models.CharField(max_length=11, choices=TypeChoice.choices)

    icon = models.ImageField(upload_to='workout/icon/')

    break_between_approaches = models.IntegerField()

    break_after_exercise = models.IntegerField()

    number = models.IntegerField(default=1000)

    workout = models.ForeignKey('workout.WorkoutModel', on_delete=models.CASCADE, related_name='exercises')

    path_to_user = 'workout__user'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stabilization_field_number(workout=self.workout)
        check_link_approach_type(self)

    class Meta:
        db_table = 'workout__exercise'
        ordering = ['number']


class ApproachModel(models.Model, CheckUserModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    working_weight = models.IntegerField()

    repetitions = models.IntegerField(null=True)

    duration = models.IntegerField(null=True)

    number = models.PositiveIntegerField(default=1000)

    exercise = models.ForeignKey('workout.ExerciseModel', on_delete=models.CASCADE, related_name='approaches')

    path_to_user = 'exercise__workout__user'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        check_type(self)
        stabilization_field_number(exercise=self.exercise)

    class Meta:
        db_table = 'workout__approach'
        ordering = ['number']


def check_link_approach_type(exercise):
    appr = ApproachModel.objects.filter(exercise=exercise)
    for a in appr:
        a.save()


def check_type(approach):
    exercise = approach.exercise
    if exercise.type == 'repetitions':
        if approach.repetitions is None:
            approach.repetitions = approach.duration
            approach.duration = None
            approach.save()
            if approach.repetitions is None:
                raise ValidationError("Поле repetitions не должно быть Null")
    elif exercise.type == 'time':
        if approach.duration is None:
            approach.duration = approach.repetitions
            approach.repetitions = None
            approach.save()
            if approach.duration is None:
                raise ValidationError("Поле duration не должно быть Null")


def stabilization_field_number(workout=None, exercise=None):
    if workout:
        objs = ExerciseModel.objects.filter(workout=workout)
    elif exercise:
        objs = ApproachModel.objects.filter(exercise=exercise)
    else:
        assert workout is None and exercise is None
    list_obj = objs.values_list('number', flat=True)
    if [i for i in objs.values_list('number', flat=True)] == list(range(1, len(list_obj)+1)):
        for o in objs:
            if o.number is None:
                o.number = max([i for i in objs.values_list('number', flat=True)]) + 1
        return
    else:
        now = 0
        objs = list(objs)
        while objs:
            o = min(objs, key=lambda x: x.number)
            if o.number == now + 1:
                objs.remove(o)
                now += 1
            else:
                o.number = now + 1
                o.save()
                objs.remove(o)
                now += 1
        return
