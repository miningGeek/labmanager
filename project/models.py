from django.db import models

# Create your models here.

project_priority_list = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ]

status = [
    ('Planning', 'Planning'),
    ('Ready', 'Ready'),
    ('In-progress', 'In-progress'),
    ('On-hold', 'On-hold'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
]
suffix = [
    ('A', 'A'),
('B', 'B'),
('C', 'C'),
('D', 'D'),
('E', 'E'),
('F', 'F'),
('G', 'G'),
('H', 'H'),
('I', 'I'),
('J', 'J'),
('K', 'K'),
('L', 'L'),
('M', 'M'),
('N', 'N'),
]

shift = [
    ('FD', 'FD'),
    ('AM', 'AM'),
    ('PM', 'PM'),
    ('NS', 'NS'),
]

pulverise = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Other', 'Other'),
]

class ProjectOwners(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    email_address = models.CharField(max_length=250, blank=True)
    status_active = models.BooleanField(default=True)
    project_owner_concat_name = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.project_owner_concat_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_owner_concat_name


class Project(models.Model):
    project_number = models.CharField(max_length=50)
    project_suffix = models.CharField(max_length=10, choices=suffix, default="A")
    project_owner = models.ForeignKey(ProjectOwners, on_delete=models.CASCADE, blank=True)
    project_priority = models.CharField(max_length=20, choices=project_priority_list, default='1')
    project_status = models.CharField(max_length=25, choices=status, default='Planning')
    project_creation_date = models.DateField(auto_now_add=True)
    project_created_by = models.CharField(max_length=50)
    project_modified_by = models.CharField(max_length=50, null=True)
    project_modified_date = models.DateField(blank=True, null=True)
    project_concated_name = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.project_concated_name = f"{self.project_number} {self.project_suffix}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_concated_name


class Technician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    email_address = models.CharField(max_length=250, blank=True)
    technician_concat_name = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.technician_concat_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.technician_concat_name


class TestList(models.Model):
    test = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.test


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_suffix = models.CharField(max_length=10, choices=suffix, default="A")
    task_description = models.CharField(max_length=5000)
    task_critical_path = models.IntegerField(default=1000)
    task_group = models.ForeignKey(TestList, on_delete=models.CASCADE, default="Nil")
    task_assigned_to = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=True, null=True)
    task_due_date = models.DateField()
    task_created_by = models.CharField(max_length=30, blank=True)
    task_creation_date = models.DateTimeField(auto_now_add=True)
    task_status = models.CharField(max_length=25, choices=status, default='Planning')
    task_shift = models.CharField(max_length=25, choices=shift, default='FD')
    task_start_date = models.DateField(blank=True, null=True)
    task_end_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_pan = models.CharField(max_length=30)
    task_modified_by = models.CharField(max_length=50, blank=True, null=True)
    task_modified_date = models.DateField(blank=True, null=True)
    task_concated_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.task_name



class AssayDetails(models.Model):
    pulverise = models.CharField(max_length=10, choices=pulverise, default='Yes')
    assay_method = models.CharField(max_length=200)

    def __str__(self):
        return self.assay_method





