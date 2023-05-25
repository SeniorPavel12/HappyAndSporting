from django.urls import path
from rest_framework_simplejwt.views import token_refresh, token_verify, token_obtain_pair

from user.api.views import CreateUserAPIView

urlpatterns = [
    path('create_user/', CreateUserAPIView.as_view()),
    path('get_pair_token/', token_obtain_pair),
    path('refresh_token/', token_refresh),
]