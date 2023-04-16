from django.urls import path,include
from .views import ProductCreate, ProductList

urlpatterns = [
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('list/', ProductList.as_view(), name='product_list'),
]
