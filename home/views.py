import random
import calendar
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse

from .utils import quotes
from django.contrib.auth.decorators import login_required
from project.models import Project, Task, ProjectOwners
from .decorators import unauthenticated_user, allowed_users, admin_only

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from datetime import datetime
# Create your views here.

#just adding a note to hopefully push to server for a restart
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

    try:
        pm_first_name = request.user.first_name
        pm_last_name = request.user.last_name
        pm_name = pm_first_name + ' ' + pm_last_name
        pm_user = ProjectOwners.objects.get(project_owner_concat_name=pm_name)
        planning_project_count = Project.objects.filter(project_owner=pm_user, project_status='Planning' ).count()
        ready_project_count = Project.objects.filter(project_owner=pm_user, project_status='Ready').count()
        progress_project_count = Project.objects.filter(project_owner=pm_user, project_status='In-progress').count()
        hold_project_count = Project.objects.filter(project_owner=pm_user, project_status='On-hold').count()
        completed_project_count = Project.objects.filter(project_owner=pm_user, project_status='Completed').count()

        if request.user.username == "jenT":
            length = len(quotes)
            rand_quote = random.randint(0, length)
            quote = quotes[rand_quote - 1]
            context = {
                'planning_project_count': planning_project_count,
                'ready_project_count': ready_project_count,
                'progress_project_count': progress_project_count,
                'hold_project_count': hold_project_count,
                'completed_project_count': completed_project_count,
                'quote': quote,
            }
        else:
            context = {
                'planning_project_count': planning_project_count,
                'ready_project_count': ready_project_count,
                'progress_project_count': progress_project_count,
                'hold_project_count': hold_project_count,
                'completed_project_count': completed_project_count,

            }
        return render(request, 'home.html', context)
    except ProjectOwners.DoesNotExist as e:
        pm_first_name = request.user.first_name
        pm_last_name = request.user.last_name
        pm_name = pm_first_name + ' ' + pm_last_name
        print(pm_name)

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


@login_required(login_url='home_app:login')
def monthly_report_form(request):
    return render(request, 'home/monthly_report_form.html')


@login_required(login_url='home_app:login')
def generate_monthly_report(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    month_name = calendar.month_name[int(month)]

    #find first day of month
    start_date= datetime.strptime(f"{year}-{month}-01","%Y-%m-%d").date()

    #find last day of month
    if month == '12':
        end_date = datetime.strptime(f"{int(year)+1}-01-01", "%Y-%m-%d").date()
    else:
        end_date = datetime.strptime(f"{year}-{int(month)+1}-01", "%Y-%m-%d").date()

    filename = f'monthly_report_{month}_{year}.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    canv = canvas.Canvas(response, pagesize=A4)

    #draw logo to report
    img_path = "static/images/core-logo.png"
    img = ImageReader(img_path)
    img_width, img_height = img.getSize()
    canv.drawImage(img, 0, A4[1] - img_height, width=img_width, height=img_height)

    #get the number of tasks created etc in a selected month and year
    task_month_created = Task.objects.filter(task_creation_date__gte=start_date, task_creation_date__lt=end_date).count()
    task_month_completed = Task.objects.filter(task_creation_date__gte=start_date, task_creation_date__lt=end_date, task_status='Completed').count()
    task_month_planning = Task.objects.filter(task_creation_date__gte=start_date, task_creation_date__lt=end_date,
                                               task_status='Planning').count()
    task_month_progress = Task.objects.filter(task_creation_date__gte=start_date, task_creation_date__lt=end_date,
                                              task_status='In-progress').count()

    #Title Section
    canv.setFillColorRGB(255, 255, 255)
    canv.setStrokeColorRGB(0.5, 0.5, 0.5)
    margin = 20
    title_rect_height = 40
    title_rect_y = 715
    title_rect_width = A4[0] - 2 * margin
    title_text = f"Laboratory Monthly Report for {month_name} {year}"
    canv.rect(margin, title_rect_y, title_rect_width, title_rect_height, stroke=1, fill=1)
    canv.setFillColorRGB(0, 0, 0)
    canv.setFont('Helvetica-Bold', 20)
    canv.drawString(margin + 10, title_rect_y + 15, title_text)

    #Body Section
    canv.setFont("Helvetica", 12)  # set font size back to 12
    canv.drawString(50, 680, f"This report provides a summary analysis of the Core Laboratory")
    canv.drawString(50, 650, f"The total amount of tasks created for the month was: {task_month_created}")
    canv.drawString(50, 630, f"The number of tasks completed for the month was: {task_month_completed}")
    canv.drawString(50, 610, f"The number of tasks in Planning state is: {task_month_planning}")
    canv.drawString(50, 590, f"The number of tasks in In-Progess state is: {task_month_progress}")
    canv.drawString(50, 575, f"The number of Sample Prep tasks created is: ")
    canv.drawString(50, 560, f"The number of Sample Prep tasks completed is: ")
    canv.save()
    return response
