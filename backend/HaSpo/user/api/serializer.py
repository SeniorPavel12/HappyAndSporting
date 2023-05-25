from django.contrib.auth import get_user_model
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validate_data):
        username, password = validate_data['username'], validate_data['password']
        instance = self.Meta.model.objects.create_user(username, password)
        return instance

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')