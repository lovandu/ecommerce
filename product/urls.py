from django import views
from django.urls import path, include
from .views import*
app_name='product'
urlpatterns = [
    path('', GetProduct.as_view(), name='product'),
]