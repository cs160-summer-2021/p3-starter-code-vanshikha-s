from django.urls import path

from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('new/interaction/', views.new_interaction, name='new_interaction'),
    path('template/options/', views.template_options, name='template_options'),
    path('do/not/disturb/', views.do_not_disturb, name='do_not_disturb'),
    path('done/', views.done, name='done'),
    path('exit/message/', views.exit_message, name='exit_message'),
   

   
]
