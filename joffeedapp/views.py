from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import JOF
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required    
def jofarchive(request):
    jofs = JOF.objects.all().order_by('-date')
    return render(request, 'joffeed/archivedJOFs.html', {"jofs":jofs})

@login_required
def jofcurrent(request):
    jofs = JOF.objects.all().order_by('status')
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})

@login_required
def jofrush(request):
    jofs = JOF.objects.all().order_by('date')
    return render(request, 'joffeed/rushJOFs.html', {"jofs":jofs})

@login_required
def jofsettings(request):
    return render(request, 'joffeed/settingsJOF.html')

@login_required
def joffeed(request):
    jofs = JOF.objects.all().order_by('date')
    return render(request, 'joffeed/JOFfeed.html', {"jofs":jofs})

@login_required
def jofview(request, pk):
    jof = JOF.objects.get(id=pk)
    return render(request, 'joffeed/viewJOF.html', {"jof":jof})

@login_required
def jofcreate(request):
    return render(request, 'joffeed/createJOF.html')