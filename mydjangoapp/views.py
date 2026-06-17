from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepageview(request):
    return render(request, 'home.html')

def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')

def shoppageview(request):
    return render(request, 'shop.html')
 
def contactprocess(request):
    if request.method == 'POST':
        a = request.POST['txt1']
        b = request.POST['txt2']
        msg = "your name is " , a , " and your email is " , b,
        return HttpResponse(msg)
    
