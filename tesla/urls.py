from django.urls import path
from .views import Page

urlpatterns = [
    path('', Page.as_view(), name='main'),
]