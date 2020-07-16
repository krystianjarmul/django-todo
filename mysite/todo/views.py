from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by("-id")

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return redirect("/")

def task_update(request, pk):
    task = Task.objects.get(id=pk)


def task_completed(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()

    return redirect('/')