from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def template_options(request):
    return render(request, 'coloring/template_options.html')