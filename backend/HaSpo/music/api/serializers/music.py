from rest_framework import serializers

from music.models import MusicModel


class DeleteMusicSerializer(serializers.Serializer):
    id = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=MusicModel.objects.all()))

    def save(self):
        _data = []
        instances = self.validated_data['id']
        for instance in instances:
            _data.append(instance)
            instance.delete()
        return _data


class CreateMusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicModel
        fields = ['title', 'content', 'playlist']
        extra_kwargs = {'playlist': {"required": False, "allow_empty": True}}


class UpdateMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = ['title', 'playlist']
        extra_kwargs = {'playlist': {"required": False, "allow_empty": True}}


class GetAllMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = ['id', 'title', 'playlist']
        extra_kwargs = {'playlist': {"allow_null": True}}


class GetMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = ['id', 'title', 'content', 'playlist']
        extra_kwargs = {'playlist': {"allow_null": True}}
