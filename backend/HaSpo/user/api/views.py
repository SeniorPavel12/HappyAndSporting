from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


from user.api.serializer import CreateUserSerializer


class CreateUserAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = request.data
        serializer = CreateUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data, status=status.HTTP_200_OK)
