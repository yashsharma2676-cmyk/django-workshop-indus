from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepageview(request):
    return render(request, 'home.html')

def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')
