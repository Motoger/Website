from .models import Task, Profile
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task','prise']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите значение'}),
                   'task': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                    'prise': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите сроки'}),
                   }

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['about_me','contact']
        widgets = {'about_me': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите значение'}),
                   'contact': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите значение'}),
                   }
