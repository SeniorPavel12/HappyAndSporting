from functools import wraps

from django.db import transaction
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from HaSpo.constans import RequestError
from music.models import CheckUserModelMixin


def check_exception(func):
    @wraps(func)
    def checking_exception(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except RequestError as exc:
            return Response({"detail": exc.args}, status=status.HTTP_400_BAD_REQUEST)
        return result

    return checking_exception


def check_validate_user(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        def check_user(o):
            assert isinstance(o, CheckUserModelMixin)
            flag = o.check_user(user)
            return flag
        assert isinstance(args[1], Request)
        assert hasattr(args[1], 'user')
        user = args[1].user
        with transaction.atomic():
            result = func(*args, **kwargs)
        try:
            control_data = result.data.pop('_control_data')
        except KeyError:
            raise ValueError("Если используется декоратор check_validate_user в ответе должен присутствовать ключ _control_data содержащий все используемые записи бд")
        assert isinstance(control_data, (list, tuple))
        if all(map(check_user, control_data)):
            return result
        transaction.set_rollback(True)
        raise RequestError(
            "Вы можете взаимодействовать только с теми объекты которые принадлежат вашему текущему пользователю")

    return decorator
