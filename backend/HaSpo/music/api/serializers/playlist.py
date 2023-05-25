from rest_framework import serializers

from music.models import PlaylistModel


class DeletePlaylistSerializer(serializers.Serializer):
    id = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=PlaylistModel.objects.all()))

    def save(self):
        _data = []
        instances = self.validated_data['id']
        for instance in instances:
            _data.append(instance)
            instance.delete()
        return _data


class CreatePlaylistSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return PlaylistModel.objects.create(**validated_data)

    class Meta:
        model = PlaylistModel
        fields = ['title']


class UpdatePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistModel
        fields = ['title']


class GetAllPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistModel
        fields = ['id', 'title']


class GetPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistModel
        fields = ['id', 'title']
