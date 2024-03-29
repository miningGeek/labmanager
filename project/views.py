from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .models import Project, Task, ProjectOwners, Technician, TestList, TaskEdit, EditReason
from .forms import AddProjectForm, AddProjectOwner, AddTestForm, AddTechnician, AddTaskForm, EditTestForm, EditProjectForm,\
    FullEditTaskForm,EditProjectOwner,ScheduleEditTaskForm,CoordEditProjectForm, AddEditReasonForm, ReasonFullEditTaskForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.views.generic import View

from home.decorators import unauthenticated_user, allowed_users


@login_required(login_url='home_app:login')
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
        user_data = {'project_created_by': request.user.username}
        form = AddProjectForm(initial=user_data)

    context = {
        'project_list': project_list,
        'form': form,

    }
    return render(request, 'project/home.html', context)


@login_required(login_url='home_app:login')
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


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def coord_edit_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = CoordEditProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_app:project_home_page')

    context = {
        "project": project,
        'form': form,
    }
    return render(request, 'project/coord_edit_project.html', context)


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return redirect('project_app:project_home_page')


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
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


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
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


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def delete_project_owner(request, project_owner_id):
    project_owner = ProjectOwners.objects.get(pk=project_owner_id)
    project_owner.delete()
    return redirect('project_app:project_owners')


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
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


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def edit_test_list(request, test_id):
    test_list = TestList.objects.get(pk=test_id)
    form = EditTestForm(request.POST or None, instance=test_list)
    if form.is_valid():
        form.save()
        return redirect('project_app:test_list')
    context = {
        'form': form,
    }
    return render(request, 'project/edit_test_list.html', context)


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def delete_test_list(request, test_id):
    test_list = TestList.objects.get(pk=test_id)
    test_list.delete()
    return redirect('project_app:test_list')


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
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


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def delete_technician(request, technician_id):
    tech = Technician.objects.get(pk=technician_id)
    tech.delete()
    return redirect('project_app:technician_list')


@login_required(login_url='home_app:login')
def task_home_page(request):
    task_list = Task.objects.all().exclude(Q(task_status='Completed') | Q(task_status='Cancelled')).order_by('project__project_priority', 'task_critical_path')

    return render(request, 'project/task_home_page.html', {
        'task_list': task_list,
    })


@login_required(login_url='home_app:login')
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
        user_data = {'task_created_by': request.user.username}
        form = AddTaskForm(initial=user_data)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'project/add_task.html', {'form': form, 'submitted': submitted})


@login_required(login_url='home_app:login')
def pm_edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = AddTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()

        # create a new TaskEdit instance to track the edit
        edit_reason = EditReason.objects.create(edit_reason='PM Changed')
        edit = TaskEdit(
            task=task,
            edited_by=request.user,
            edit_reason=edit_reason,
        )
        edit.save()

        return redirect('project_app:task_home_page')
    context = {
        "task": task,
        'form': form,
    }
    return render(request, 'project/pm_edit_task.html', context)


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def full_edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        if task.task_assigned_to:
            form = ReasonFullEditTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                edit = TaskEdit(
                    task=task,
                    edited_by=request.user,
                    edit_reason = EditReason.objects.create(edit_reason=form.cleaned_data['edit_reason']),

                )
                edit.save()
                return redirect('project_app:task_home_page')
        else:
            form = FullEditTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('project_app:task_home_page')
    else:
        if task.task_assigned_to:
            form = ReasonFullEditTaskForm(instance=task)
        else:
            form = FullEditTaskForm(instance=task)
    context = {
        "task": task,
        "form": form,
    }
    return render(request, 'project/full_edit_task.html', context)


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def schedule_edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if 'submit_form' in request.POST:
        form = ScheduleEditTaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('schedule_app:schedule_home')
    if 'copy_task' in request.POST:
        form = ScheduleEditTaskForm(request.POST or None, instance=task)
        task.pk = None
        task.id = None
        if form.is_valid():
            form.save()
            return redirect('schedule_app:schedule_home')
    form = ScheduleEditTaskForm(request.POST or None, instance=task)
    context = {
        "task": task,
        'form': form,
    }
    return render(request, 'project/schedule_edit_task.html', context)

@allowed_users(allowed_roles=['Coordinator'])
def task_pdf(request, task_id):
    task = Task.objects.get(pk=task_id)
    pm_name = task.project.project_owner

    template_path = 'project/task_pdf.html'
    context = {
        'task': task,
        'pm_name': pm_name,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename="task.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + '</pre>')

    return response



def test(request):
    return render(request, 'project/test.html')


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def viewTaskEdit(request):
    edit_reason_list = EditReason.objects.all()

    if request.method == "POST":
        form = AddEditReasonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('edit_reason_list')
    else:
        form = AddEditReasonForm

    context = {
        'edit_reason_list': edit_reason_list,
        'form': form,

    }
    return render(request, 'project/edit_reason_list.html', context)


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def delete_edit_reason(request, edit_id):
    edit_reason = EditReason.objects.get(pk=edit_id)
    edit_reason.delete()
    return redirect('project_app:edit_reason_list')


@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def modify_edit_reason(request, edit_id):
    edit_id = EditReason.objects.get(pk=edit_id)
    form = AddEditReasonForm(request.POST or None, instance=edit_id)
    if form.is_valid():
        form.save()
        return redirect('project_app:edit_reason_list')
    context = {
        'form': form,
    }
    return render(request, 'project/modify_edit_reason.html', context)


def task_edit_track(request):
    track_edit_list = TaskEdit.objects.all()
    context = {
        'track_edit_list': track_edit_list,
    }
    return render(request, 'project/task_edit_track.html', context)



