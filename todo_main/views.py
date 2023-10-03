from todo.models import Task 
from django.shortcuts import render
#from django.http import HttpResponse


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks1': tasks ,
    }
    return render(request, 'home.html', context)