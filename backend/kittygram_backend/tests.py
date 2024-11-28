from http import HTTPStatus

from api import models
from django.test import Client, TestCase

class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности списка котиков."""
        response = self.guest_client.get('/api/cats/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка добавления котика."""
        data = {'name': 'Test', 'owner': 'Test'}
        response = self.guest_client.post('/api/cats/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
