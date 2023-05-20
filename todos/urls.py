from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(),name="todo_detail"),
    path('', ListTodo.as_view(), name="todo_list"),
]