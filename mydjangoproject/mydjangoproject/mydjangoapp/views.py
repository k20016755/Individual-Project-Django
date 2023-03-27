from django.shortcuts import render
from mydjangoapp.models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'mydjangoapp/task_list.html', {'tasks': tasks})
# Create your views here.
