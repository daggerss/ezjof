from django.shortcuts import render
from django.http import HttpResponse
from .models import JOF

def home(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})
    
def jofarchive(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/archivedJOFs.html', {"jofs":jofs})

def jofcurrent(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})

def jofpending(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/pendingJOFs.html', {"jofs":jofs})

def jofrush(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/rushJOFs.html', {"jofs":jofs})

def jofsettings(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/settingsJOF.html', {"jofs":jofs})

