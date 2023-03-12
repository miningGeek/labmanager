from django import forms
from django.forms import ModelForm, DateField, widgets, ModelChoiceField
from project.models import Task, Project, Technician, ProjectOwners, TestList




class ScheduleEditTask(ModelForm):

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_suffix",
                  "task_assigned_to",
                  "task_start_date",
                  "task_end_date",

                  )
        labels = {
            "project": "Project Number",
            "task_name": "Name",
            "task_assigned_to": "Tech Assigned",
            "task_start_date": "Start Date",
            "task_end_date": "Finish Date",

        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required', 'style':'width:150px; height:30px'}),
            'task_start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style':'width:150px; height:30px'}),
            'task_end_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style':'width:150px; height:30px'}),

        }




class ScheduleFindTask(forms.Form):
    taskfind = ModelChoiceField(queryset=Task.objects.all())

    class Meta:
        model = Task
        fields =(
            "taskfind",
        )


class testForm(forms.Form):

    class Meta:
        model = Task
        fields =(
            "task_id",
            "task_name",
        )


