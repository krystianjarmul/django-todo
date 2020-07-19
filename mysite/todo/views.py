from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpRequest, HttpResponse

from .models import Task
from .forms import TaskForm


def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("-id")

    form = TaskForm()

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})


def task_delete(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    task.delete()

    return redirect("/")


def task_update(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    tasks = Task.objects.all().order_by("-id")

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})


def task_completed(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()

    return redirect('/')
