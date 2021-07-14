from django.urls import path

from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('new/interaction/one/', views.new_interaction_one, name='new_interaction_one'),
    path('new/interaction/two/', views.new_interaction_two, name='new_interaction_two'),
    path('template/options/', views.template_options, name='template_options'),
    path('do/not/disturb/', views.do_not_disturb, name='do_not_disturb'),
    path('done/', views.done, name='done'),
    path('exit/message/', views.exit_message, name='exit_message'),
    path('save/reminder/one/', views.save_reminder_one, name='save_reminder_one'),
    path('save/reminder/two/', views.save_reminder_two, name='save_reminder_two'),
   

   
]
