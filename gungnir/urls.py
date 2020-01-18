
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('visualize/', views.visualize, name = 'visualize'),
    path('predict/', views.predict, name = 'predict')
]
