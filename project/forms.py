from django import forms
from django.forms import ModelForm, DateField, widgets

from .models import Project, Task, Technician, ProjectOwners, TestList


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("project_number",
                  "project_suffix",
                  "project_owner",
                  "project_priority",
                  "project_created_by")
        labels = {
            "project_number": "Project No.",
            "project_suffix": "Project Suffix",
            "project_owner": "Owner",
            "project_priority": "Project Priority",
            "project_created_by": "Created By",
        }
        widgets = {

        }


class EditProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("project_number",
                  "project_suffix",
                  "project_owner",
                  "project_priority",
                  "project_status",
                  "project_created_by")
        labels = {
            "project_number": "Project No.",
            "project_suffix": "Project Suffix",
            "project_owner": "Owner",
            "project_priority": "Project Priority",
            "project_status": "Project Status",
            "project_created_by": "Created By",
        }
        widgets = {

        }


class AddProjectOwner(ModelForm):
    class Meta:
        model = ProjectOwners
        fields = (
            "first_name",
            "last_name",
            "email_address"
        )
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email_address": "Email Address",
        }


class EditProjectOwner(ModelForm):
    class Meta:
        model = ProjectOwners
        fields = (
            "first_name",
            "last_name",
            "email_address",
            "status_active"
        )
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email_address": "Email Address",
            "status_active": "Active/ Not Active",
        }



class AddTestForm(ModelForm):
    class Meta:
        model = TestList
        fields = (
            "test",
        )
        widgets = {
            "test": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }





class AddTechnician(ModelForm):
    class Meta:
        model = Technician
        fields = (
            "first_name",
            "last_name",

        )
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",

        }


class AddTaskForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select Project Number")
    task_group = forms.ModelChoiceField(queryset=TestList.objects.all().order_by('test'), empty_label="Select Test")

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_suffix",
                  "task_group",
                  "task_critical_path",
                  "task_due_date",
                  "task_description",
                  )
        labels = {
            "project": "Project Number",
            "task_name": "Name",
            "task_group": "Test Group",
            "task_description": "Description",
            "task_critical_path": "Critical Path No.",
            "task_due_date": "Due Date",
            "task_created_by": "Created By",
            "task_creation_date": "Date Created",

        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            "task_critical_path": forms.TextInput(attrs={'class': 'form-control'}),
            "task_description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_due_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "task_created_by": forms.TextInput(attrs={'class': 'form-control'}),
            'task_creation_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }


class FullEditTaskForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select Project Number")
    task_group = forms.ModelChoiceField(queryset=TestList.objects.all().order_by('test'), empty_label="Select Test")

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_suffix",
                  "task_group",
                  "task_critical_path",
                  "task_due_date",
                  "task_status",
                  "task_assigned_to",
                  "task_start_date",
                  "task_end_date",
                  "task_description",
                  "task_created_by",
                  )
        labels = {
            "project": "Project Number",
            "task_name": "Name",
            "task_group": "Test Group",
            "task_description": "Description",
            "task_critical_path": "Critical Path No.",
            "task_due_date": "Due Date",
            "task_created_by": "Created By",
            "task_creation_date": "Date Created",
            "task_status": "Task Status",
            "task_assigned_to": "Tech Assigned",
            "task_start_date": "Start Date",
            "task_end_date": "Finish Date",
            "task_created_by": "Created By"

        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            "task_critical_path": forms.TextInput(attrs={'class': 'form-control'}),
            "task_description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_due_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "task_created_by": forms.TextInput(attrs={'class': 'form-control'}),
            'task_creation_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_end_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }

class ScheduleEditTask(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select Project Number")
    task_group = forms.ModelChoiceField(queryset=TestList.objects.all().order_by('test'), empty_label="Select Test")

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_suffix",
                  "task_group",
                  "task_critical_path",
                  "task_status",
                  "task_assigned_to",
                  "task_start_date",
                  "task_end_date",

                  )
        labels = {
            "project": "Project Number",
            "task_name": "Name",
            "task_group": "Test Group",
            "task_description": "Description",
            "task_critical_path": "Critical Path No.",
            "task_due_date": "Due Date",
            "task_created_by": "Created By",
            "task_creation_date": "Date Created",
            "task_status": "Task Status",
            "task_assigned_to": "Tech Assigned",
            "task_start_date": "Start Date",
            "task_end_date": "Finish Date",
            "task_created_by": "Created By"

        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            "task_critical_path": forms.TextInput(attrs={'class': 'form-control'}),
            "task_description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_due_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "task_created_by": forms.TextInput(attrs={'class': 'form-control'}),
            'task_creation_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_end_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }