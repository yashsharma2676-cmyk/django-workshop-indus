from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview ),  
    path('home', views.homepageview, ),    
    path('about', views.aboutview),
    path('contact', views.contactview),
    path('contactprocess', views.contactprocess),
    path('savesessiondata', views.savesessiondata),
    path('getsessiondata', views.getsessiondata),
    path('deletesessiondata', views.deletesessiondata),
    path('login', views.loginpage),
    path('loginprocess', views.loginprocess),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('shop', views.shoppageview),
    path('marks', views.marksview),
    path('marksheetprocess', views.marksheetprocess, name='marksheetprocess'),

   
]