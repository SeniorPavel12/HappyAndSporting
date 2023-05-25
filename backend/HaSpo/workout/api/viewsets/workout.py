from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

from music.api.viewsets.mixin import *
from workout.api.serializers import *
from workout.api.service import *
from workout.models import WorkoutModel, ExerciseModel


class WorkoutViewSet(ViewSet, DeleteViewSetMixin, CreateViewSetMixin, UpdateViewSetMixin, GetAllViewSetMixin,
                     GetViewSetMixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    basename = 'workout'

    get_instance = get_workout_instance
    get_all_instances = get_all_workout_instances

    get_serializer = GetWorkoutSerializer
    get_all_serializer = GetAllWorkoutSerializer
    update_serializer = UpdateWorkoutSerializer
    create_serializer = CreateWorkoutSerializer
    delete_serializer = DeleteWorkoutSerializer

    readable_name = 'workout'
    model = WorkoutModel
    link_field = None

    @action(detail=False, methods=['post'], url_path='get_not_free_workout_color', renderer_classes=[JSONRenderer])
    @check_exception
    def get_not_free_workout_color(self, request):
        """Ничего не принимает, возвращает уже занятые цвета workout для данного пользователя({'color': [color,
        color, ...]})"""
        user = request.user
        data = get_not_free_workout_color(user)
        response = {'color': data}
        return Response(response)


class ExerciseViewSet(ViewSet, DeleteViewSetMixin, CreateViewSetMixin, UpdateViewSetMixin, GetAllViewSetMixin,
                      GetViewSetMixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    basename = 'exercise'

    get_instance = get_exercise_instance
    get_all_instances = get_all_exercise_instances

    get_serializer = GetExerciseSerializer
    get_all_serializer = GetAllExerciseSerializer
    update_serializer = UpdateExerciseSerializer
    create_serializer = CreateExerciseSerializer
    delete_serializer = DeleteExerciseSerializer

    readable_name = 'exercise'
    model = ExerciseModel
    link_field = 'workout'


class ApproachViewSet(ViewSet, DeleteViewSetMixin, CreateViewSetMixin, UpdateViewSetMixin, GetAllViewSetMixin,
                      GetViewSetMixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    basename = 'approach'

    get_instance = get_approach_instance
    get_all_instances = get_all_approach_instances

    get_serializer = GetApproachSerializer
    get_all_serializer = GetAllApproachSerializer
    update_serializer = UpdateApproachSerializer
    create_serializer = CreateApproachSerializer
    delete_serializer = DeleteApproachSerializer

    readable_name = 'approach'
    model = ApproachModel
    link_field = 'exercise'
