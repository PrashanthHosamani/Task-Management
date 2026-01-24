from django.shortcuts import render
from todo.models import Uncomplted_Task

def home(request):
    tasks = Uncomplted_Task.objects.filter(is_completed = False)
    context = {
        
        "tasks" : tasks,
        
    }
    return render(request, 'home.html', context)

