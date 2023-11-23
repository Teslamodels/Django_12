from django.urls import path
from .views import Steve

urlpatterns = [
    path('apple', Steve.as_view(), name='steve'),
]