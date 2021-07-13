from django.urls import path

from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('new/interaction/', views.new_interaction, name='new_interaction'),
]