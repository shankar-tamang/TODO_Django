from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
            return redirect('login.html')

        else:
            return redirect('signin')

def signut(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') 
    
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        print(fname, lname, uname, email, password)
        User.objects.create_user(username=uname, password=password, email=email, fname=fname, lname=lname)


        return render(request, 'register.html')
