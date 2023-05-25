from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from HaSpo.constans import RequestError
from HaSpo.constans.decorator import check_validate_user, check_exception

"""Для всех классов предположительно используется MultiPartParser"""


class GetViewSetMixin:
    get_instance = None
    get_serializer = None

    @action(detail=False, methods=['post'], url_path='get', renderer_classes=[JSONRenderer])
    @check_exception
    @check_validate_user
    def custom_get(self, request):
        """Принимает id объекта и возвращает все данные о нём"""
        _data = []
        try:
            id = request.data.dict()['id']
        except KeyError:
            raise RequestError("Вы должны передать id объекта которое хотите получить")
        instance = self.get_instance(id)
        _data.append(instance)
        serializer = self.get_serializer(instance)
        response = serializer.data
        response.update({'_control_data': _data})
        return Response(response)


class UpdateViewSetMixin:
    get_instance = None
    update_serializer = None
    get_serializer = None

    @action(detail=False, methods=['post'], url_path='update', renderer_classes=[JSONRenderer])
    @check_exception
    @check_validate_user
    def custom_update(self, request):
        """Принимает данные для обновления объекта + id объекта, возвращает сериализованный обновлённый объект"""
        _data = []
        data = request.data
        try:
            id = data['id']
        except KeyError:
            raise RequestError("В теле запроса должно быть поле id объекта которое вы хотите изменять")
        instance = self.get_instance(id)
        serializer = self.update_serializer(instance, data=data, partial=True) #partial=True тк в сериализаторах все поля обязательны
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        _data.append(instance)
        serializer = self.get_serializer(instance)
        response = serializer.data
        response.update({'_control_data': _data})
        return Response(response)


class CreateViewSetMixin:
    create_serializer = None

    @action(detail=False, methods=['post'], url_path='create', renderer_classes=[JSONRenderer])
    @check_exception
    @check_validate_user
    def custom_create(self, request):
        """Принимает данные для создания объекта, возвращает id созданного объекта"""
        _data = []
        data = request.data
        user = request.user
        serializer = self.create_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        if self.model.path_to_user == 'user':
            instance = serializer.save(user=user) #надо передать user тк пользователь его не отправляет, но только тогда когда требует этого модель
        else:
            instance = serializer.save()
        _data.append(instance)
        response = {'id': instance.id}
        response.update({'_control_data': _data})
        return Response(response)


class GetAllViewSetMixin:
    link_field = None #Показывает поле по которому будут искаться все связанные объекты при запросе get_all(если None значит все объекты)(строка)
    readable_name = None #Показывает имя которое будет использовать как ключ к списку при запросе get_all(строка)
    get_all_instances = None
    get_all_serializer = None

    @action(detail=False, methods=['post'], url_path='get_all', renderer_classes=[JSONRenderer])
    @check_exception
    @check_validate_user
    def custom_get_all(self, request):
        """Ничего не принимает или принимает id связанного объекта по которому будет искаться ответ, возвращает основные данные о найденных объектах"""
        _data = []
        user = request.user
        data = request.data
        if self.link_field is not None:
            try:
                id = data['id']
            except KeyError:
                raise RequestError("Вы должны передать id связанного объекта на основании которого будут искаться объекты")
            instances = self.get_all_instances(user, link_field=self.link_field, link_id=id)
        else:
            instances = self.get_all_instances(user)
        _data.extend(instances)
        serializer = self.get_all_serializer(instances, many=True)
        response = {self.readable_name: serializer.data}
        response.update({'_control_data': _data})
        return Response(response)


class DeleteViewSetMixin:
    delete_serializer = None

    @action(detail=False, methods=['post'], url_path='delete', renderer_classes=[JSONRenderer])
    @check_exception
    @check_validate_user
    def custom_delete(self, request):
        """Принимает id объектов которые надо удалить вида: {"id": [id, id, id...]}, возвращает тело запроса))"""
        _data = []
        data = dict(request.data)

        serializer = self.delete_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        _data.extend(serializer.save())
        data.update({'_control_data': _data})
        return Response(data)
