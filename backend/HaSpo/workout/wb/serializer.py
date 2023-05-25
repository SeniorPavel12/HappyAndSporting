import uuid

from rest_framework import serializers

from HaSpo.constans import RequestError
from workout.logic.events import RequestEvent
from workout.models import WorkoutModel


class RequestSerializer(serializers.Serializer):
    workout = serializers.CharField(required=False)
    type = serializers.CharField()

    async def create(self, validated_data):
        type = validated_data['type']
        print('cre1')
        if type == 'SW':
            workout_id = validated_data['workout']
            workout = await WorkoutModel.objects.aget(id=uuid.UUID(workout_id))
        else:
            workout = None
        print('cre2')
        if type == 'SW' and workout is None:
            print('cre3')
            raise RequestError("Если type SW то workout is not None")
        elif type != 'SW' and workout is not None:
            print('cre4')
            raise RequestError("Если type не SW то workout is  None")
        print('createser')
        return RequestEvent(type, workout)

class ResponseSerializer(serializers.Serializer):
    type = serializers.CharField()
    data = serializers.DictField()
    other_data = serializers.DictField()
