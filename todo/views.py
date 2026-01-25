from django.shortcuts import redirect, get_object_or_404
from .models import Uncompleted_Task
from django.http import HttpResponse

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Uncompleted_Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Uncompleted_Task, pk = pk) #this function will fetch the data from the database if its exist or return 404 error (no need of try and expect)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Uncompleted_Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')



