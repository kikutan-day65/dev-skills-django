from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})

def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        # check if the form is valid
        if form.is_valid():
            form.save() # create an object
            return redirect('projects')  # redirect to the designated path

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)    # get the specific project with using pk
    form = ProjectForm(instance=project)    # take the project as an instance, this will pre-fill in the form

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        # check if the form is valid
        if form.is_valid():
            form.save() # create an object
            return redirect('projects')  # redirect to the designated path

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)