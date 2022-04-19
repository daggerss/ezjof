from django.shortcuts import render
from django.http import HttpResponse
from .models import JOF
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})

@login_required    
def jofarchive(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/archivedJOFs.html', {"jofs":jofs})

@login_required
def jofcurrent(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})

@login_required
def jofrush(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/rushJOFs.html', {"jofs":jofs})

@login_required
def jofsettings(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/JOFfeed.html', {"jofs":jofs})

def jofview(request):
    return render(request, 'joffeed/JOFview.html')