from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'projects'
    num = 10
    context = {
        'page': page,
        'num': num,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single-project.html')