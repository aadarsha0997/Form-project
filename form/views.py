from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and conform password is not matching")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
    return render(request,"form/signup.html")



def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            return HttpResponse("User name or Password is incorrect!!")
    return render(request,"form/login.html")

@login_required(login_url='/login/') # Specify the URL to redirect unauthenticated users to the login page
def home_page(request):
    return render(request,"form/home.html")
    
def logout_page(request):
    auth_logout(request)
    return redirect('user_login')