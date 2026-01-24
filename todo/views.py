from django.shortcuts import redirect
from .models import Uncompleted_Task

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Uncompleted_Task.objects.create(task=task)
    return redirect('home')

