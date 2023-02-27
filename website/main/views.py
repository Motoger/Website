from django.shortcuts import render
from .models import Task, Profile
from .forms import TaskForm

def index(request):
    task=Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главная страница', 'tasks': task})

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    prof=Profile.objects.all()
    return render(request, 'main/profile.html',{'title':'Профиль', 'profs': prof})

def create(request):
    form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'main/create.html', context)