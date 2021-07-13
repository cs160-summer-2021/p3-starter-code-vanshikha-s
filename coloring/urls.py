from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('demo/', views.demo, name='demo'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('new/interaction/', views.new_interaction, name='new_interaction'),
    path('template_options', views.template_options, name='template_options')
   
]
=======
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('template_options', views.template_options, name='template_options')
]
>>>>>>> origin
