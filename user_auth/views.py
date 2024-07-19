from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else: 
        uname = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=uname, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')
        

def signout(request):
    logout(request)
    return redirect('signin')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')     
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=uname, password=password, email=email, first_name=fname, last_name=lname, is_staff=False, is_superuser=False)

        if user is not None:
            return redirect('signin')
        
        else:
            return redirect('register')


