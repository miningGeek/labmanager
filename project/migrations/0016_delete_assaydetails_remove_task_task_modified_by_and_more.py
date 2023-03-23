# Generated by Django 4.1.5 on 2023-03-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_rename_task_due_date_task_task_request_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssayDetails',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_modified_by',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_modified_date',
        ),
        migrations.AddField(
            model_name='task',
            name='assay_method',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_assay_loc',
            field=models.CharField(choices=[('Internal', 'Internal'), ('External', 'External'), ('Other', 'Other')], default='Internal', max_length=15),
        ),
        migrations.AddField(
            model_name='task',
            name='task_pulverise',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Other', 'Other')], default='No', max_length=10),
        ),
    ]