from django.shortcuts import render

def task_list(request):
    return render(request, 'todo/task_list.html')