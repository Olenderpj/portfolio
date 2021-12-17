from django.shortcuts import render, redirect
from .models import Project
from .forms import CreateProjectForm

# Create your views here.

def index(request):
    all_projects = Project.objects.all()
    total_projects = Project.objects.all().count()

    context = {
        'all_projects': all_projects,
        'total_projects': total_projects,
    }

    return render(request, 'index.html', context=context)


def projectCreateView(request):
    form = CreateProjectForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'newProject.html', context=context)


def projectShowView(request, id):
    project = Project.objects.get(pk=id)

    context = {
        'project': project
    }
    return render(request, 'showProject.html', context=context)

def deleteProject(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    return redirect('/')

def deleteAllProjects(request):
    allProjects = Project.objects.all()
    allProjects.delete()
    return redirect('/')

