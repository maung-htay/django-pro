from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'product_create.html'
    

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'    

