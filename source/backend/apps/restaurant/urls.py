from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.apply_restaurant, name='apply-restaurant'),
]