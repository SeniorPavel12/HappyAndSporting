from asgiref.sync import sync_to_async
from channels.generic.websocket import JsonWebsocketConsumer
from django.db import transaction
from rest_framework.exceptions import APIException

from HaSpo.constans import RequestError
from workout.logic.gengerator import main_handle
from workout.wb.base import JsonPermissionConsumer, IsAuthenticatedPermission
from workout.wb.serializer import RequestSerializer, ResponseSerializer


class RunWorkoutConsumer(JsonPermissionConsumer):
    # permissions_classes = [IsAuthenticatedPermission]

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive_json(self, content, **kwargs):
        try:
            print(1)
            serializer = RequestSerializer(data=content)
            print(2)
            await sync_to_async(serializer.is_valid)(raise_exception=True)
            print(3)
            request = await serializer.save()
            if request.type == 'SW' and 'main_handle_gen' in self.scope.keys():
                raise RequestError("Вы уже начали тренировку")
            if request.type in ["NT", "EW"] and 'main_handle_gen' not in self.scope.keys():
                raise RequestError("Сначала начните тренировку")
            if 'main_handle_gen' not in self.scope.keys():
                self.scope['main_handle_gen'] = main_handle()
                await self.scope['main_handle_gen'].asend(None)
            print(5)

            instance = await self.scope['main_handle_gen'].asend(request)
            if type(instance) == list:
                many = True
            else:
                many = False
            serializer = ResponseSerializer(instance=instance, many=many)
            response = serializer.data
            print(5.5)
            if many:
                for s in range(len(response)):
                    response[s] = dict(response[s])
            print(6)
            await self.send(f"{response}")
        except RequestError as exc:
            response = exc.args
            await self.send(f'''{{"error": {response}}}''')
        except APIException as exc:
            response = exc.args
            await self.send(f'''{{"error": {response}}}''')








"""
Принимаем данные(content) обрабатываем их(сериализуем и валидируем), затем создаем объект RequestEvent чтобы 
инкапсулировать все данные в один объект и соединить данные с функцией а также понять тип запроса, потом передаём 
объект RequestEvent в сопрограмму в которой находим какое действие выполнять(скорее всего это старт тренировки 
окончание след действие(упражнение или перерыв), если след действие генерируем его если окончание завершаем 
сопрограмму выводя какие либо результаты, ответ полученный от сопрограммы инкапсулируем в ResponseEvent сериализуем 
его и отправляем клиенту)
"""
