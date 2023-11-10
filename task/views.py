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