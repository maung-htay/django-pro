from django.urls import path
from .views import HomePageVeiw

urlpatterns = [
    path("", HomePageVeiw.as_view(), name="home")
]
