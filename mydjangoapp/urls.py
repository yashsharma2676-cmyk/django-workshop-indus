from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview ),  
    path('home', views.homepageview, ),    
    path('about', views.aboutview),
    path('contact', views.contactview),
]