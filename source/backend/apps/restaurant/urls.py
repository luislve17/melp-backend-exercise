from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.apply_restaurant, name='apply-restaurant'),
    path('statistics/', views.get_stats, name='get-stats'),
]