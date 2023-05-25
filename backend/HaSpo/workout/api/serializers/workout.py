from rest_framework import serializers

from workout.models import WorkoutModel


class DeleteWorkoutSerializer(serializers.Serializer):
    id = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=WorkoutModel.objects.all()))

    def save(self):
        _data = []
        instances = self.validated_data['id']
        for instance in instances:
            _data.append(instance)
            instance.delete()
        return _data


class CreateWorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutModel
        fields = ['name', 'color', 'icon', 'initial_break', 'playlist']
        extra_kwargs = {'playlist': {"required": False}}


class UpdateWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutModel
        fields = ['name', 'color', 'icon', 'initial_break', 'playlist']


class GetAllWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutModel
        fields = ['id', 'name', 'color', 'icon']


class GetWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutModel
        fields = ['id', 'name', 'color', 'icon', 'initial_break', 'playlist']
        extra_kwargs = {'playlist': {"allow_null": True}}
