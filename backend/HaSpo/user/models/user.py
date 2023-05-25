import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserModel(AbstractUser):
    id = models.UUIDField(
        'id',
        primary_key=True,
        default=uuid.uuid4
    )

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
    )

    email = models.EmailField(
        "email",
        blank=True,
        null=True
    )
