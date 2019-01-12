from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm

""" Project Views """

# Get All Project


def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard.html', {'projects': projects})

# Get One Project
def project(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project.html', {'project': project, 'tasks': project.tasks.all()})

# Create New Project
def newProject(request):
    if request.method == 'GET':
        return render(request, 'newProject.html')

    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            budget = form.cleaned_data['budget']
            description = form.cleaned_data['description']
            due_date = form.cleaned_data['due_date']

            Project.objects.create(
                name=name,
                budget=budget,
                description=description,
                due_date=due_date
            ).save()

        return redirect('/')


# Delete Project
def deleteProject(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('/')


""" Task Views """
# Create Task
def newTask(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        id = request.POST.get("project")
        name = form.cleaned_data['name']
        expense = form.cleaned_data['expense']
        category = form.cleaned_data['category']
        status = form.cleaned_data['status']
        description = form.cleaned_data['description']

        project = get_object_or_404(Project, id=id)

        Task.objects.create(
            project=project,
            name=name,
            expense=expense,
            category=category,
            status=status,
            description=description
        ).save()

    return redirect('project', id)

# Update Task
def finishTask(request, id, project):
    task = get_object_or_404(Task, id=id)
    task.status = 'Finished'
    task.save()
    return redirect('project', project)


# Delete Task
def deleteTask(request, id, project):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('project', project)
