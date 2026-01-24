from django.shortcuts import render
from todo.models import Uncompleted_Task

def home(request):
    tasks = Uncompleted_Task.objects.filter(is_completed = False).order_by("-updated_at")
    
    completed_tasks = Uncompleted_Task.objects.filter(is_completed = True)
    context = {
        
        "tasks" : tasks,
        "completed_tasks" : completed_tasks,
        
    }
    return render(request, 'home.html', context)

