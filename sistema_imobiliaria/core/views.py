from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def residenciais(request):
    return render(request, 'core/residenciais.html')
