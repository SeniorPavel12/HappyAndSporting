from rest_framework.routers import SimpleRouter

from workout.api.viewsets.workout import *


router = SimpleRouter()
router.register('workout', WorkoutViewSet, basename='workout')
router.register('exercise', ExerciseViewSet, basename='exercise')
router.register('approach', ApproachViewSet, basename='approach')
urlpatterns = [] + router.urls

