from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model

disconnect_code = [
    (402, "Unauthorized")
]


class JsonPermissionConsumer(AsyncJsonWebsocketConsumer):
    permissions_classes = []

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        for perm in self.permissions_classes:
            flag = perm(text_data, self.scope)
            if flag is False:
                await self.disconnect(perm.disconnect_code)
        await super().receive(text_data, bytes_data, **kwargs)


class IsAuthenticatedPermission:
    disconnect_code = 402

    def __call__(self, data, scope):
        user = scope.get('user', None)
        if user is None:
            return False
        return isinstance(user, get_user_model())
