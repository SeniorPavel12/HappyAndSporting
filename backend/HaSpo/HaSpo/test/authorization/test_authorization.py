import io

from django.test import TestCase
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from rest_framework.renderers import JSONRenderer
from django.test import Client

class TestToken(TestCase):
    username = 'pavel'
    password = '123456789!'
    client = Client()

    def setUp(self):
        get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_create_user(self):
        url = '/api/user/create_user/'
        username = 'root'
        password = '123456789!'
        data = {'username': username, 'password': password}
        response = self.client.post(url, data=data)
        parser = JSONParser()
        content = parser.parse(io.BytesIO(response.content))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(content, {'username': username, 'password': password})
        self.assertEquals(len(get_user_model().objects.filter(username=username)), 1)

    def test_get_pair_token_and_refresh_token(self):
        url1 = '/api/user/get_pair_token/'
        url2 = '/api/user/refresh_token/'
        response = self.client.post(url1, {'username': self.username, 'password': self.password})
        parser = JSONParser()
        content = parser.parse(io.BytesIO(response.content))
        self.assertEquals(response.status_code, 200)
        self.assertIn('access', content.keys())
        self.assertIn('refresh', content.keys())
        response = self.client.post(url2, content)
        content = parser.parse(io.BytesIO(response.content))
        self.assertEquals(response.status_code, 200)
        self.assertIn('access', content.keys())




