# from channels.auth import AuthMiddleware
# from django.contrib.auth.models import AnonymousUser
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.exceptions import TokenError
#
#
# class TokenAuthMiddleware(JWTAuthentication):
#
#     def __init__(self, inner):
#         print(1)
#         self.inner = inner
#
#     def __call__(self, scope):
#         print(2)
#         print('TokenAuthMiddleware')
#         headers = dict(scope['headers'])
#         if b'authorization' in headers:
#             token_val, token_key = headers[b'authorization'].decode().split()
#
#             try:
#                 validated_token = self.get_validated_token(token_val)
#                 user = self.get_user(validated_token), validated_token
#                 scope["user"] = user
#             except TokenError:
#                 scope["user"] = AnonymousUser()
#         else:
#             scope["user"] = AnonymousUser()
#         return self.inner(scope)
#
#
# TokenMiddleware = lambda inner: TokenAuthMiddleware(AuthMiddleware(inner))
