from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview ),  
    path('home', views.homepageview, ),    
    path('about', views.aboutview),
    # path('contact', views.contactview),
    # path('contactprocess', views.contactprocess),
    path('savesessiondata', views.savesessiondata),
    path('getsessiondata', views.getsessiondata),
    path('deletesessiondata', views.deletesessiondata),
    path('login', views.loginpage),
    path('loginprocess', views.loginprocess),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('contact', views.contactpage),
    path('contactprocess', views.contactpageprocess),
    path('shop', views.shoppageview),
    path('marks', views.marksview),
    path('marksheetprocess', views.marksheetprocess, name='marksheetprocess'),
    path('addstudent',views.addstudentform,name='addstudent'),
    path('add_student_process',views.addstudentformprocess),
    path('add-category/', views.add_category, name='add_category' ),
    path('display-category/', views.display_category, name='display_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit_product'),
     path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),


   
]