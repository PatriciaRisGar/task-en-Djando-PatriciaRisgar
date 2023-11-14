from django.shortcuts import redirect, render
from django.views import View
from .forms import TaskForm
from .models import Task

# Create your views here.
"""
def tasks_list(request):

    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()

    return render(request, 'task/tasks_list.html', {'tasks': tasks, 'form':form})
"""
"""
class TaskView(View):
    tasks = Task.objects.all()
    templateList = 'task/tasks_list.html'

    def actualizaTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get (self,request):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, self.templateList, {'tasks': tasks, 'form':form})
    
    def post (self,request):
        form = TaskForm(request.POST)
        tasks = Task.objects.all()
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
        return render(request, self.templateList, {'tasks': tasks, 'form':form})
"""

from django.shortcuts import render

from .forms import TaskForm


def TaskView(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            realizada = form.cleaned_data['realizada']
            Task.objects.create(nombre=nombre,descripcion=descripcion,realizada=realizada)
            return redirect('tasks_list')
        return render(request, "task/tasks_list.html", {'tasks': tasks, 'form':form})

    else:
        form = TaskForm()

    return render(request, "task/tasks_list.html", {'tasks': tasks, 'form':form})