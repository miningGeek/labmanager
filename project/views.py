from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Project, Task, ProjectOwners, Technician, TestList
from .forms import AddProjectForm, AddProjectOwner, AddTestForm, AddTechnician, AddTaskForm, EditProjectForm,\
    FullEditTaskForm,EditProjectOwner
from django.db.models import Q
# Create your views here.


def home(request):
    project_list = Project.objects.all().exclude(Q(project_status="Cancelled")| Q(project_status="Completed")).order_by('project_priority','project_number')
    import requests
    import json

    if request.method == "POST":
        if 'submit_form' in request.POST:
            form = AddProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('project_home_page')
        if 'project_filter' in request.POST:
            project_status = request.POST.get('project_status')
            if project_status == "Default":
                project_list = Project.objects.all().exclude(
                    Q(project_status="Cancelled") | Q(project_status="Completed")).order_by('project_priority','project_number')
            elif project_status == "All":
                project_list = Project.objects.all()
            else:
                project_list = Project.objects.filter(project_status=project_status)

            form = AddProjectForm
            context = {
                'project_list': project_list,
                'form': form,
            }
            return render(request, 'project/home.html', context)
    else:
        form = AddProjectForm

    context = {
        'project_list': project_list,
        'form': form,

    }
    return render(request, 'project/home.html', context)


def edit_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = EditProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_app:project_home_page')

    context = {
        "project": project,
        'form': form,
    }
    return render(request, 'project/edit_project.html', context)


def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return redirect('project_app:project_home_page')


def project_owners(request):
    project_owner_list = ProjectOwners.objects.filter(status_active=True)
    import requests
    import json

    if request.method == "POST":
        if 'submit_form' in request.POST:
            form = AddProjectOwner(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('project_owners')
        if 'project_owner_status' in request.POST:
            owner_status = request.POST.get('project_owner_status')
            if owner_status == "True":
                project_owner_list = ProjectOwners.objects.filter(status_active=True)
            elif owner_status == "False":
                project_owner_list = ProjectOwners.objects.filter(status_active=False)
            elif owner_status == "Default":
                project_owner_list = ProjectOwners.objects.all()
            form = AddProjectOwner
            context = {
                'project_owner_list': project_owner_list,
                'form': form,
            }
            return render(request, 'project/project_owner.html', context)

    else:
        form = AddProjectOwner

    context = {
        'project_owner_list': project_owner_list,
        'form': form,

    }
    return render(request, 'project/project_owner.html', context)


def edit_project_owner(request, project_owner_id):
    project_owner = ProjectOwners.objects.get(pk=project_owner_id)
    form = EditProjectOwner(request.POST or None, instance=project_owner)
    if form.is_valid():
        form.save()
        return redirect('project_app:project_owners')
    context = {
        'form': form,
    }
    return render(request, 'project/edit_project_owner.html', context)


def delete_project_owner(request, project_owner_id):
    project_owner = ProjectOwners.objects.get(pk=project_owner_id)
    project_owner.delete()
    return redirect('project_app:project_owners')


def test_list(request):
    tests = TestList.objects.all().order_by('test')
    import requests
    import json

    if request.method == "POST":
        form = AddTestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('test_list')
    else:
        form = AddTestForm

    context = {
        'tests': tests,
        'form': form,
    }
    return render(request, 'project/test_list.html', context)


def technician_list(request):
    tech_list = Technician.objects.all()
    import requests
    import json

    if request.method == "POST":
        form = AddTechnician(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('technician_list')
    else:
        form = AddTechnician

    context = {
        'tech_list': tech_list,
        'form': form,

    }
    return render(request, 'project/technician_list.html', context)


def task_home_page(request):
    task_list = Task.objects.all().exclude(task_status='Completed').order_by('project', 'task_critical_path')

    return render(request, 'project/task_home_page.html', {
        'task_list': task_list,
    })


def add_task(request):
    import requests
    import json
    submitted = False
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('task_home_page?submitted=True')
    else:
        form = AddTaskForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'project/add_task.html', {'form': form, 'submitted': submitted})


def full_edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = FullEditTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('project_app:task_home_page')

    context = {
        "task": task,
        'form': form,
    }
    return render(request, 'project/full_edit_task.html', context)








