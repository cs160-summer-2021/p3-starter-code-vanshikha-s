from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return render(request, 'coloring/demo.html')

def index(request):
    return render(request, 'coloring/index.html')

def info(request):
    return render(request, 'coloring/info.html')

def new_interaction(request):
    return render(request, 'coloring/comparison-alert.html')