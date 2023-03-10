# Generated by Django 4.1.5 on 2023-01-27 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=50)),
                ('project_suffix', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default='A', max_length=10)),
                ('project_priority', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=20)),
                ('project_status', models.CharField(choices=[('Planning', 'Planning'), ('Ready', 'Ready'), ('In-progress', 'In-progress'), ('On-hold', 'On-hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Planning', max_length=25)),
                ('project_creation_date', models.DateField()),
                ('project_created_by', models.CharField(max_length=50)),
                ('project_modified_by', models.CharField(max_length=50)),
                ('project_modified_date', models.DateField(blank=True)),
                ('project_concated_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectOwners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('email_address', models.CharField(blank=True, max_length=250)),
                ('project_owner_concat_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('email_address', models.CharField(blank=True, max_length=250)),
                ('technician_concat_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_suffix', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default='A', max_length=10)),
                ('task_description', models.CharField(max_length=1000)),
                ('task_critical_path', models.IntegerField(default=1000)),
                ('task_due_date', models.DateField()),
                ('task_created_by', models.CharField(blank=True, max_length=30)),
                ('task_creation_date', models.DateTimeField(auto_now_add=True)),
                ('task_status', models.CharField(choices=[('Planning', 'Planning'), ('Ready', 'Ready'), ('In-progress', 'In-progress'), ('On-hold', 'On-hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Planning', max_length=25)),
                ('task_start_date', models.DateField(blank=True, null=True)),
                ('task_end_date', models.DateField(blank=True, null=True)),
                ('task_modified_by', models.CharField(max_length=50)),
                ('task_modified_date', models.DateField(blank=True)),
                ('task_concated_name', models.CharField(blank=True, max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('task_assigned_to', models.ForeignKey(blank=True, default='Nobody', on_delete=django.db.models.deletion.CASCADE, to='project.technician')),
                ('task_group', models.ForeignKey(default='Nil', on_delete=django.db.models.deletion.CASCADE, to='project.testlist')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='project.projectowners'),
        ),
    ]
