from django.contrib import admin
from django.urls import path, include

from .views import PostDetail, PostList

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]