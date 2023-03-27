from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'mydjangoapp/task_list.html', {'tasks': tasks})
# Create your views here.
