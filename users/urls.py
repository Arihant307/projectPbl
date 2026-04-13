from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('stores/', views.store_list, name='store_list'),
]