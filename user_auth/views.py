from django.shortcuts import render

# Create your views here.

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else: 

        uname = request.POST['username']
        password = request.POST['password']

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
        return render(request, 'register.html')
