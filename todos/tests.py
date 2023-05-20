from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models  import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.todo = Todo.objects.create(title='test title', description='test description')