from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import student 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def homepageview(request):
    return render(request, 'home.html')

def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')

def marksview(request):
    return render(request, 'marksheet.html')

# def mailsenddemo(request):
#     subject='Django mail demo'
#     message='aur kii haal paaji?'
#     email_from=settings.EMAIL_HOST_USER
#     recipient_list=['yashsharma2676@gmail.com']
#     send_mail(subject, message, email_from, recipient_list)
#     return HttpResponse("Mail sent successfully")
 
def contactpage(request):
    return render(request, 'contact.html')

def contactpageprocess(request):
       
   txt1 = request.POST['txt1']
   txt2 = request.POST['txt2']
   txt3 = request.POST['txt3']
   txt4 = request.POST['txt4']
   
   mymsg="Hello you are contacted by",txt1
   mymsg+="Mobile number:",txt2
   mymsg+="Email:",txt3
   mymsg+="Message:",txt4

   subject = 'Contact us from website'
   email_from = settings.EMAIL_HOST_USER

   message = mymsg
   recipient_list = ['yash@gmail.com']
   send_mail(subject, message, email_from, recipient_list)
   return HttpResponse("Thankyou for contacting us.")
    
   
def savesessiondata(request):
    request.session['username']="Yash Sharma"
    return HttpResponse("Session data saved")

def getsessiondata(request):
    if request.session.has_key('username'):
        msg=request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("Session data not found")
    
def deletesessiondata(request):
    del request.session['username']
    return HttpResponse("Session data deleted")

def loginpage(request):
    return render(request, 'login.html')

def loginprocess(request):
    txt1=request.POST['email']
    request.session['email']=txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('email'):
        return render(request, "dashboard.html")
    else:
        return redirect(loginpage)

def logout(request):
    del request.session['email']
    return redirect(loginpage)

# def contactprocess(request):
#     a=int(request.POST['txt1'])
#     b=int(request.POST['txt2'])
#     c=a+b
#     d=""
#     if c==30:
#         d="IF condition is called"
#     elif c<40:
#         d="ELIF condition is called"
#     else:
#         d="ELSE condition is called"
#     return render(request, "ans.html", {"mya": a, "myb": b, "myc": c, "myd": d})

def shoppageview(request):
    return render(request, 'shop.html')

def marksheetprocess(request):
    a=int(request.POST["txt1"])
    b=int(request.POST["txt2"])
    c=int(request.POST["txt3"])
    d=int(request.POST["txt4"])
    e=int(request.POST["txt5"])
    total=a+b+c+d+e
    percentage=(total/500)*100
    if percentage>=90:
        grade="A"   
    elif percentage>=80:
        grade="B"   
    elif percentage>=70:
        grade="C"
    elif percentage>=60:
        grade="D"
    else:
        grade="F"
    return render(request, "marks.html", {"mya": a, "myb": b, "myc": c, "myd": d, "mye": e, "mytotal": total, "mypercentage": percentage, "mygrade": grade})

def addstudentform(request):
    return render(request,'add_student.html')

def addstudentformprocess(request):
    txt1=request.POST['txt1']
    txt2=request.POST['txt2']
    txt3=request.POST['txt3']
    txt4=request.POST['txt4']
    student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    mymsg="Hello you are contacted by",txt1
    mymsg+="Mobile number:",txt2
    mymsg+="Email:",txt3
    mymsg+="Message:",txt4

    subject = 'Contact us from website'
    email_from = settings.EMAIL_HOST_USER

    message = mymsg
    recipient_list = ['yashs@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    mymsg="Hello",txt1
    mymsg+="Mobile number:",txt2
    mymsg+="Email:",txt3
    mymsg+="Message:",txt4

    subject = 'you Contacted us from website'
    email_from = settings.EMAIL_HOST_USER

    message = mymsg
    recipient_list = [txt3]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Thankyou for contacting us.")

def add_category(request):
    if request.method == "POST":
        txt1 = request.POST['txt1']
        Category.objects.create(title=txt1)
        return redirect('add_category')
    return render(request, 'add-category.html')

def display_category(request):
    categorylist = Category.objects.all()
    return render(request, 'display-category.html', {'category': categorylist})

def delete_category(request, id):
    Category.objects=get(id=id).delete()
    return redirect('display-category')

def edit_category(request, id):
    category = Category. objects.get(id=id)
    if request.method == "POST":
        category.title = request. POST['txt1']
        category . save ()
        return redirect('display_category')
    return render(request, 'edit-category.html', {'category': category})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login')
    
#def mailstudent(request):
    return render(request, 'mail.html')

#def mailstudentform(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
   


