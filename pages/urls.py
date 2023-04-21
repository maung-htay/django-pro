from django.urls import path
from .views import HomePageVeiw, AboutPageVeiw

urlpatterns = [
    path("about/", AboutPageVeiw.as_view(), name="about"),
    path("", HomePageVeiw.as_view(), name="home"),
  
]
