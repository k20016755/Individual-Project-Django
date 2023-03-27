from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'mydjangoproject/mydjangoapp/templates/task_list.html', {'tasks': tasks})
# Create your views here.
