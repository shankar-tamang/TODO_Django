from django.shortcuts import render, redirect
from main.models import TODO

# Create your views here.

def home(request):
    todos = TODO.objects.all()
    return render(request, 'main/home.html', {'todos':todos})


def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')


def add_blog(request):

    if request.method == 'GET':
        return render(request, 'main/add_blog.html')
        # request.method
    else:
        title = request.POST['title']  
        desc = request.POST['description']
        TODO.objects.create(title=title, content=desc, is_completed=False, user_id=1)
        return redirect('http://127.0.0.1:8000/')




