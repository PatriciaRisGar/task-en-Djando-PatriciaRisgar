from django.shortcuts import render
from .models import Task

# Create your views here.

def tasks_list(request):

    tasks = Task.objects.all()
    return render(request, 'task/tasks_list.html', {'tasks': tasks})