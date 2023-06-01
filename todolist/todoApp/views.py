from django.shortcuts import render, redirect, get_object_or_404
from todoApp.models import Task

def index(request):
    return render(request, "index.html")


def list(request):
    tasks = Task.objects.all()
    return render(request, 'list.html', {'tasks': tasks})


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save() 
        return redirect('list') 
    return render(request, 'add.html')

def edit(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task.title = title
        task.description = description
        task.save()
        return redirect('list')
    return render(request, 'edit.html', {'task': task})

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('list')


