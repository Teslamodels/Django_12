from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Bill(TemplateView):
    template_name = 'micro.html'