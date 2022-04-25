from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import JOF
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
    form=JOFForm
    if request.method=='POST':
        form=JOFForm(request.POST)
        if form.is_valid():
            new_isrush = form.cleaned_data['isrush']
            new_name = form.cleaned_data['name']
            new_description = form.cleaned_data['description']
            new_date = form.cleaned_data['date']
            new_pegs = form.cleaned_data['pegs']
            new_summary = form.cleaned_data['summary']
            new_type = form.cleaned_data['type']
            new_spiel = form.cleaned_data['spiel']
            new_JOF = JOF.objects.create(status = JOF.NOT_TAKEN, isrush = new_isrush, name = new_name,description = new_description,date = new_date,pegs = new_pegs,summary = new_summary,type = new_type,spiel = new_spiel)
            new_JOF.save()
            form=JOFForm
            return render(request, 'joffeed/createJOF.html',{'form':form})
    return render(request, 'joffeed/createJOF.html',{'form':form})