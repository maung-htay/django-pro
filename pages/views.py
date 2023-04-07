from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageVeiw(TemplateView):
    template_name = "home.html"
