from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('example/', views.example, name='example'),
    path('bar/', views.bar, name='bar'),
    path('donut/', views.donut, name='donut'),
    path('radar/', views.radar, name='radar'),
    path('line/', views.line, name='line'),
    path('scutter/', views.scutter, name='scutter'),
    path('pie/', views.pie, name='pie'),
]
