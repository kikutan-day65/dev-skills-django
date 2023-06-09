from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm, ReviewForm
from .utils import search_project, paginate_projects

def projects(request):

    projects, search_query =  search_project(request)

    custom_range, projects = paginate_projects(request, projects, 6)
    
    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.get_vote_count

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})

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
            return redirect('account')  # redirect to the designated path

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
            return redirect('account')  # redirect to the designated path

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
    return render(request, 'delete_template.html', context)