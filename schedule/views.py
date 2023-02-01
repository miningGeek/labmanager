from django.shortcuts import render
from django.apps import apps
from project.models import Task, Project

import plotly.express as px
import pandas as pd
# Create your views here.


def schedule_home(request):



    morning_colour = 'rgb(29, 133, 60)'
    afternoon_colour = 'rgb(29, 133, 60)'
    model_task = apps.get_model('project', 'Task')
    data_gantt = {'Tasks': [], 'Start': [], 'Finish': [], 'Resource': []}
    task_list = Task.objects.all().exclude(task_status = 'Completed')
    for task in task_list:
        data_gantt['Tasks'].append(task.task_name)
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



    # set the x axis to show all days/dates instead of skipping - https://stackoverflow.com/questions/34755707/how-to-show-all-x-axis-tick-values-in-plotly
    fig.update_xaxes(tickmode='linear')
    fig.update_yaxes(autorange="reversed")
    # Loop to show a multilayerd gantt with a morning or afternoon wrap to help visualise if a job is less than a day.
    # Still need to add code to change the morning/afternoon colours to a fixed colour for each to help with consitencies.
    for i in range(len(df.index)):
        if df.iloc[i].Resource == 'M':
            fig.data[i].width=1.1
        if df.iloc[i].Resource == 'A':
            fig.data[i].width = 1.1

    fig.update_layout(title={
        'font_size': 22,
        'xanchor': 'center',
        'x': 0.5
    })
    fig.update_yaxes(autorange="reversed")
    chart = fig.to_html()

    context = {
        "chart": chart,

    }
    return render(request, 'schedule/schedule_home.html', context)