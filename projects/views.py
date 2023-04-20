from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        # check if the form is valid
        if form.is_valid():
            project = form.save(commit=False) # create an object
            project.owner = profile
            project.save()
            return redirect('projects')  # redirect to the designated path

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)    # get the specific project with using pk
    form = ProjectForm(instance=project)    # take the project as an instance, this will pre-fill in the form

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        # check if the form is valid
        if form.is_valid():
            form.save() # create an object
            return redirect('projects')  # redirect to the designated path

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)