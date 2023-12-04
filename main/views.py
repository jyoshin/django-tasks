from django.shortcuts import render, get_object_or_404, redirect
from . models import Task

def home(request):
    all_tasks = Task.objects.all()
    return render(request, 'main/home.html', {'all_tasks': all_tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completion = request.POST.get('completion') == 'on'

        Task.objects.create(title=title, description=description, completion=completion)

        return redirect('home')
    
    return render(request, 'main/add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completion = request.POST.get('completion') == 'on'
        task.save()

        return redirect('home')
    
    return render(request, 'main/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        
        return redirect('home')
    
    return render(request, 'main/delete_task.html', {'task': task})