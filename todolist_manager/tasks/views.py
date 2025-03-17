from django.shortcuts import render, redirect
from .forms import TaskForm
from .services import TaskService
from .managers import DjangoTaskManager
from .display import HtmlTaskDisplay
from .sorters import PrioritySorter

# Create service with dependency injection
task_service = TaskService(
    task_manager=DjangoTaskManager(),
    task_display=HtmlTaskDisplay(),
    task_sorter=PrioritySorter()
)

def task_list(request):
    status = request.GET.get('status')
    status_filter = None
    if status == 'completed':
        status_filter = True
    elif status == 'pending':
        status_filter = False
    
    tasks = task_service.get_tasks(status=status_filter, sort=True)
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'status': status or 'all'
    })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_service.create_task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                priority=form.cleaned_data['priority']
            )
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/add_task.html', {'form': form})

def complete_task(request, task_id):
    task_service.complete_task(task_id)
    return redirect('task_list')

def delete_task(request, task_id):
    task_service.delete_task(task_id)
    return redirect('task_list')