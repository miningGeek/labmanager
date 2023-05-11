from django import forms
from django.forms import ModelForm, DateField, widgets

from .models import Project, Task, Technician, ProjectOwners, TestList, EditReason


class AddProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ("project_number",
                  "project_suffix",
                  "project_owner",
                  "project_created_by")
        labels = {
            "project_number": "Project No.",
            "project_suffix": "Project Suffix",
            "project_owner": "Owner",
            "project_created_by": "Created By",
        }
        widgets = {
            "project_created_by": forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        proj_owner_query = self.fields['project_owner'].queryset
        proj_owner_query= proj_owner_query.exclude(status_active=False)
        self.fields['project_owner'].queryset =proj_owner_query


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
            "project_created_by": forms.TextInput(attrs={'readonly': 'readonly'}),
            "project_priority": forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class CoordEditProjectForm(ModelForm):
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
            "project_created_by": forms.TextInput(attrs={'readonly': 'readonly'}),
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


class EditTestForm(ModelForm):
    class Meta:
        model = TestList
        fields = (
            "test",
        )
        widgets = {
            "test": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }



class AddEditReasonForm(ModelForm):
    class Meta:
        model = EditReason
        fields = (
            "edit_reason",
        )
        labels = {
            "edit_reason": "Task Edit Reason",
        }
        widgets = {
            "edit_reason": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
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
                  "task_pan",
                  "task_group",
                  "task_critical_path",
                  "task_request_date",
                  "task_description",
                  "task_pulverise",
                  "task_assay_loc",
                  "assay_method",
                  "task_created_by",
                  )
        labels = {
            "project": "Project Number",
            "task_name": "Task Name",
            "task_pan": "PAN",
            "task_group": "Test Group",
            "task_description": "Description",
            "task_critical_path": "Critical Path No.",
            "task_request_date": "Request Date",
            "task_pulverise": "Pulverise Required",
            "task_assay_loc": "Assay Lab",
            "assay_method": "Assay Method Required",
            "task_created_by": "Created By",
            "task_creation_date": "Date Created",

        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            "task_critical_path": forms.TextInput(attrs={'class': 'form-control'}),
            "task_description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_request_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "task_created_by": forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'task_creation_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "assay_method": forms.Textarea(attrs={'class': 'form-control'}),
        }


class FullEditTaskForm(ModelForm):

    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select Project Number")
    task_group = forms.ModelChoiceField(queryset=TestList.objects.all().order_by('test'), empty_label="Select Test")
    #edit_reason = forms.ModelChoiceField(queryset=EditReason.objects.all().order_by('edit_reason'), empty_label="Select Reason for Edit")

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_pan",
                  "task_suffix",
                  "task_group",
                  "task_critical_path",
                  "task_request_date",
                  "task_status",
                  "task_assigned_to",
                  "task_start_date",
                  "task_end_date",
                  "task_description",
                  "task_pulverise",
                  "task_assay_loc",
                  "assay_method",
                  "task_created_by",

                  )
        labels = {
            "project": "Project Number",
            "task_name": "Task Name",
            "task_pan": "PAN",
            "task_group": "Test Group",
            "task_description": "Description",
            "task_critical_path": "Critical Path No.",
            "task_request_date": "Request Date",
            "task_created_by": "Created By",
            "task_creation_date": "Date Created",
            "task_status": "Task Status",
            "task_assigned_to": "Tech Assigned",
            "task_start_date": "Start Date",
            "task_end_date": "Finish Date",
            "task_pulverise": "Pulverise Required",
            "task_assay_loc": "Assay Lab",
            "assay_method": "Assay Method Required",


        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            "task_critical_path": forms.TextInput(attrs={'class': 'form-control'}),
            "task_description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_request_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "task_created_by": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'task_creation_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_end_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "assay_method": forms.Textarea(attrs={'class': 'form-control', 'cols':80,'rows': 5}),

        }


class ReasonFullEditTaskForm(ModelForm):

    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select Project Number")
    task_group = forms.ModelChoiceField(queryset=TestList.objects.all().order_by('test'), empty_label="Select Test")
    edit_reason = forms.ModelChoiceField(queryset=EditReason.objects.all().order_by('edit_reason'), empty_label="Select Reason for Edit")

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_pan",
                  "task_suffix",
                  "task_group",
                  "task_critical_path",
                  "task_request_date",
                  "task_status",
                  "task_assigned_to",
                  "task_start_date",
                  "task_end_date",
                  "task_description",
                  "task_pulverise",
                  "task_assay_loc",
                  "assay_method",
                  "task_created_by",
                  "edit_reason",
                  )
        labels = {
            "project": "Project Number",
            "task_name": "Task Name",
            "task_pan": "PAN",
            "task_group": "Test Group",
            "task_description": "Description",
            "task_critical_path": "Critical Path No.",
            "task_request_date": "Request Date",
            "task_created_by": "Created By",
            "task_creation_date": "Date Created",
            "task_status": "Task Status",
            "task_assigned_to": "Tech Assigned",
            "task_start_date": "Start Date",
            "task_end_date": "Finish Date",
            "task_pulverise": "Pulverise Required",
            "task_assay_loc": "Assay Lab",
            "assay_method": "Assay Method Required",


        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            "task_critical_path": forms.TextInput(attrs={'class': 'form-control'}),
            "task_description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_request_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "task_created_by": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'task_creation_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_end_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "assay_method": forms.Textarea(attrs={'class': 'form-control', 'cols':80,'rows': 5}),

        }


class ScheduleEditTaskForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select Project Number")

    class Meta:
        model = Task
        fields = ("project",
                  "task_name",
                  "task_suffix",
                  "task_assigned_to",
                  "task_start_date",
                  "task_end_date",
                  "task_shift",
                  )

        labels = {
            "project": "Project Number",
            "task_name": "Name",
            "task_suffix": "Task Suffix",
            "task_status": "Task Status",
            "task_assigned_to": "Tech Assigned",
            "task_start_date": "Start Date",
            "task_end_date": "Finish Date",
            "task_shift": "Shift",


        }
        widgets = {

            "task_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'task_start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_end_date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }

