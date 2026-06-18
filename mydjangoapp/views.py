from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def homepageview(request):
    return render(request, 'home.html')

def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')

def marksview(request):
    return render(request, 'marksheet.html')

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

def contactprocess(request):
    a=int(request.POST['txt1'])
    b=int(request.POST['txt2'])
    c=a+b
    d=""
    if c==30:
        d="IF condition is called"
    elif c<40:
        d="ELIF condition is called"
    else:
        d="ELSE condition is called"
    return render(request, "ans.html", {"mya": a, "myb": b, "myc": c, "myd": d})

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



