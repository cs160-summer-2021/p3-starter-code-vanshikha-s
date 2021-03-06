from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return render(request, 'coloring/demo.html')


def index(request):
    return render(request, 'coloring/index.html')


def info(request):
    return render(request, 'coloring/info.html')


def new_interaction_one(request):
    return render(request, 'coloring/new_interaction_one.html')

def new_interaction_two(request):
    return render(request, 'coloring/new_interaction_two.html')

def template_options(request):
    return render(request, 'coloring/template_options.html')

def do_not_disturb(request):
    return render(request, 'coloring/do_not_disturb.html')

def done(request):
    return render(request, 'coloring/done.html')

def exit_message(request):
    return render(request, 'coloring/exit_message.html')

def blank_canvas_one(request):
    return render(request, 'coloring/blank_canvas_one.html')