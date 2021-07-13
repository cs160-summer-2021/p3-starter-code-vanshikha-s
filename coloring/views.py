from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return render(request, 'coloring/demo.html')

def index(request):
    return render(request, 'coloring/index.html')

<<<<<<< HEAD
def info(request):
    return render(request, 'coloring/info.html')

def new_interaction(request):
    return render(request, 'coloring/comparison-alert.html')

def template_options(request):
    return render(request, 'coloring/template_options.html')

=======
def template_options(request):
    return render(request, 'coloring/template_options.html')
>>>>>>> origin
