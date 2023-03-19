import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

from .utils import quotes
from django.contrib.auth.decorators import login_required
from project.models import Project, Task
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_app:index')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'home/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_app:login')


@login_required(login_url='home_app:login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='home_app:login')
@admin_only
def index(request):
    length = len(quotes)
    rand_quote = random.randint(0,length)
    quote = quotes[rand_quote-1]
    planning_project_count = Project.objects.filter(project_status='Planning').count()
    ready_project_count = Project.objects.filter(project_status='Ready').count()
    active_project_count = Project.objects.filter(project_status='In-progress').count()
    hold_project_count = Project.objects.filter(project_status='On-hold').count()
    completed_project_count = Project.objects.filter(project_status='Completed').count()

    planning_task_count = Task.objects.filter(task_status='Planning').count()
    ready_task_count = Task.objects.filter(task_status='Ready').count()
    active_task_count = Task.objects.filter(task_status='In-progress').count()
    hold_task_count = Task.objects.filter(task_status='On-hold').count()
    completed_task_count = Task.objects.filter(task_status='Completed').count()
    context = {
        'quote': quote,
        'planning_project_count':planning_project_count,
        'ready_project_count': ready_project_count,
        'active_project_count': active_project_count,
        'hold_project_count': hold_project_count,
        'completed_project_count': completed_project_count,
        'planning_task_count': planning_task_count,
        'ready_task_count': ready_task_count,
        'active_task_count': active_task_count,
        'hold_task_count': hold_task_count,
        'completed_task_count': completed_task_count,


    }
    return render(request, 'home/home.html', context)
