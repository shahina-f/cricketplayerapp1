from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django .contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')
def players(request):
    mem = matchlist.objects.all()
    cont = {
        'obj':mem
    }
    
    return render(request,'players.html',context=cont)
def playerlist(request,id):
    obj =playerslist.objects.get(id=id)
    dect={
        'obj':obj
    }
    print(obj)
    return render(request,'playerlist.html',context=dect)
def logindata(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def userdata(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password== cpassword:
            if fname and lname and email is not None:
                userobj=User.objects.create(first_name=fname,last_name=lname,email=email,password=password)
                userobj.save()
                return redirect(index)
    return render(request,'index.html')
def userlogin(request):
    if request.method=='POST':
     uname=request.POST.get('uname')
     password=request.POST.get('password')
     cpass=request.POST.get('cpass')
     user=authenticate(request,username=uname,password=password)
    if request.user.is_authenticated :
        login(request,user) 
        return redirect(index)
    return redirect(logindata)



