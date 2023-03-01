from django.shortcuts import render, redirect
from .models import Task, Profile
from .forms import TaskForm, ProfileForm

def index(request):
    task=Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главная страница', 'tasks': task})

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    form = ProfileForm
    prof=Profile.objects.all()
    return render(request, 'main/profile.html',{'title':'Профиль', 'profs': prof,'form':form})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'форма была не верной'
    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html', context)