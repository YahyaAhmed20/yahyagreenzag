from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()  # هيظهر حسب ترتيب الموديل
    return render(request, 'ourproject/project_list.html', {'projects': projects})

def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'ourproject/project_details.html', {'project': project})