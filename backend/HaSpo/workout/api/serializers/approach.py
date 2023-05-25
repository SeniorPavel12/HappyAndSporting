from rest_framework import serializers

from workout.models import ApproachModel


class DeleteApproachSerializer(serializers.Serializer):
    id = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=ApproachModel.objects.all()))

    def save(self):
        _data = []
        instances = self.validated_data['id']
        for instance in instances:
            _data.append(instance)
            instance.delete()
        return _data


class CreateApproachSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return ApproachModel.objects.create(**validated_data)

    class Meta:
        model = ApproachModel
        fields = ['working_weight', 'repetitions', 'duration', 'number', 'exercise']


class UpdateApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproachModel
        fields = ['working_weight', 'repetitions', 'duration', 'number']


class GetAllApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproachModel
        fields = ['id', 'working_weight', 'repetitions', 'duration', 'number']


class GetApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproachModel
        fields = ['id', 'working_weight', 'repetitions', 'duration', 'number', 'exercise']

