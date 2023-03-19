from django.shortcuts import render
from django.apps import apps
from project.models import Task, Project
from django.db.models import Q
from .forms import ScheduleEditTask, ScheduleFindTask, testForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import plotly.express as px
import pandas as pd

from home.decorators import unauthenticated_user, allowed_users
# Create your views here.

@login_required(login_url='home_app:login')
@allowed_users(allowed_roles=['Coordinator'])
def schedule_home(request):

    data_gantt = {'Tasks': [], 'Start': [], 'Finish': [], 'Resource': []}
    task_list = Task.objects.all().exclude(Q(task_status='Completed')| Q(task_status='Cancelled')).order_by('project','task_critical_path','task_suffix')
    for task in task_list:
        concat_project_task = f'{task.project} {task.task_name} ({task.task_suffix}) {task.task_shift}'
        data_gantt['Tasks'].append(concat_project_task)
        data_gantt['Resource'].append(task.task_assigned_to)
        data_gantt['Start'].append(task.task_start_date)
        data_gantt['Finish'].append(task.task_end_date)

    df = pd.DataFrame(data_gantt)
    fig = px.timeline(df,
                      x_start="Start",
                      x_end="Finish",
                      y="Tasks",
                      color="Resource",


                      labels={
                          'x': 'Date',
                          'y': 'Tasks',
                      })

    # set the x axis to show all days/dates instead of skipping -
    # https://stackoverflow.com/questions/34755707/how-to-show-all-x-axis-tick-values-in-plotly
    fig.update_xaxes(tickmode='linear', tickformat='%d %b (%a)', tickangle=300)
    fig.update_yaxes(autorange="reversed")
    # Loop to show a multilayerd gantt with a morning or afternoon wrap to help visualise if a job is less than a day.
    # Still need to add code to change the morning/afternoon colours
    # to a fixed colour for each to help with consistencies.

    # for i in range(len(df.index)):
    #     if df.iloc[i].Resource == 'M':
    #         fig.data[i].width=1.1
    #     if df.iloc[i].Resource == 'A':
    #         fig.data[i].width = 1.1
    #
    # fig.update_layout(title={
    #     'font_size': 22,
    #     'xanchor': 'center',
    #     'x': 0.5
    # })
    #fig.update_yaxes(autorange="reversed")
    chart = fig.to_html()

    form = ScheduleEditTask
    #form_task_select = ScheduleFindTask

    unassigned_tasks = Task.objects.filter(task_start_date__isnull=True)

    context = {
        "chart": chart,
        "task_list": task_list,
        "form": form,
        "unassigned_tasks": unassigned_tasks,

        #"form_task_select": form_task_select,



    }
    return render(request, 'schedule/schedule_home.html', context)

@login_required(login_url='home_app:login')
def schedule_pm(request):

        data_gantt = {'Tasks': [], 'Start': [], 'Finish': []}
        task_list = Task.objects.all().exclude(Q(task_status='Completed') | Q(task_status='Cancelled')).order_by(
            'project', 'task_critical_path', 'task_suffix')
        for task in task_list:
            concat_project_task = f'{task.project} {task.task_name} ({task.task_suffix}) {task.task_shift}'
            data_gantt['Tasks'].append(concat_project_task)
            #data_gantt['Resource'].append(task.task_assigned_to)
            data_gantt['Start'].append(task.task_start_date)
            data_gantt['Finish'].append(task.task_end_date)

        df = pd.DataFrame(data_gantt)
        fig = px.timeline(df,
                          x_start="Start",
                          x_end="Finish",
                          y="Tasks",
                          #color="Resource",

                          labels={
                              'x': 'Date',
                              'y': 'Tasks',
                          })

        # set the x axis to show all days/dates instead of skipping -
        # https://stackoverflow.com/questions/34755707/how-to-show-all-x-axis-tick-values-in-plotly
        fig.update_xaxes(tickmode='linear', tickformat='%d %b (%a)', tickangle=300)
        fig.update_yaxes(autorange="reversed")
        # Loop to show a multilayerd gantt with a morning or afternoon wrap to help visualise if a job is less than a day.
        # Still need to add code to change the morning/afternoon colours
        # to a fixed colour for each to help with consistencies.

        # for i in range(len(df.index)):
        #     if df.iloc[i].Resource == 'M':
        #         fig.data[i].width=1.1
        #     if df.iloc[i].Resource == 'A':
        #         fig.data[i].width = 1.1
        #
        # fig.update_layout(title={
        #     'font_size': 22,
        #     'xanchor': 'center',
        #     'x': 0.5
        # })
        # fig.update_yaxes(autorange="reversed")
        chart = fig.to_html()

        context = {
            "chart": chart,

        }
        return render(request, 'schedule/schedule_home.html', context)

