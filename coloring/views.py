from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return render(request, 'coloring/demo.html')


def index(request):
    return render(request, 'coloring/index.html')


def info(request):
    return render(request, 'coloring/info.html')


def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def template_options(request):
    return render(request, 'coloring/template_options.html')

def do_not_disturb(request):
    return render(request, 'coloring/do_not_disturb.html')

def done(request):
    return render(request, 'coloring/done.html')

def exit_message(request):
    return render(request, 'coloring/exit_message.html')

def save_reminder_one(request):
    return render(request, 'coloring/save_reminder_one.html')

def save_reminder_two(request):
    return render(request, 'coloring/save_reminder_two.html')