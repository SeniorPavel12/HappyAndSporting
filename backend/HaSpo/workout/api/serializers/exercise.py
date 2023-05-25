from rest_framework import serializers

from workout.models import ExerciseModel


class DeleteExerciseSerializer(serializers.Serializer):
    id = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=ExerciseModel.objects.all()))

    def save(self):
        _data = []
        instances = self.validated_data['id']
        for instance in instances:
            _data.append(instance)
            instance.delete()
        return _data


class CreateExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = ['name', 'type', 'icon', 'break_between_approaches', 'break_after_exercise', 'workout']


class UpdateExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = ['name', 'type', 'icon', 'break_between_approaches', 'break_after_exercise']


class GetAllExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = ['id', 'name', 'type', 'icon', 'number']


class GetExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = ['id', 'name', 'type', 'icon', 'break_between_approaches', 'break_after_exercise', 'number', 'workout']

