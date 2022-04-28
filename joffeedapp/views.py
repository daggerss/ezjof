from asyncio.windows_events import NULL
import email
from telnetlib import STATUS
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import JOF
from .forms import *

from loginapp.models import Account

@login_required    
def jofarchive(request):
    jofs = JOF.objects.all().order_by('-date')
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    
    
    return render(request, 'joffeed/archivedJOFs.html', {"jofs":jofs, "account":account})

@login_required
def jofcurrent(request):
    
    jofs = NULL
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    if account.type=='Client':
        jofs = JOF.objects.filter(client = account).order_by('date')
        jofs = jofs.filter(~Q(status = 4))
    elif account.type=='Artist':
        jofs = JOF.objects.filter(artist = account).order_by('date')
        jofs = jofs.filter(~Q(status = 4))
    
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs, "account":account})

@login_required
def jofrush(request):
    jofs = JOF.objects.all().order_by('date')
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    
    return render(request, 'joffeed/rushJOFs.html', {"jofs":jofs, "account":account})

@login_required
def jofsettings(request):
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    return render(request, 'joffeed/settingsJOF.html')

@login_required
def joffeed(request):
    jofs = JOF.objects.filter(status = JOF.NOT_TAKEN).order_by('date')
    
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
        
    return render(request, 'joffeed/JOFfeed.html', {"jofs":jofs, "account":account})

@login_required
def jofaccept(request, pk):
    jof = JOF.objects.get(id = pk)
    jof.status = JOF.IN_PROGRESS
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    jof.artist = account
    jof.save()
    return HttpResponseRedirect(reverse('joffeed'))

@login_required
def jofview(request, pk):
    jof = JOF.objects.get(id=pk)
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    return render(request, 'joffeed/viewJOF.html', {"jof":jof})

@login_required
def jofcreate(request):
    form=JOFForm
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
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
            new_client = account
            new_JOF = JOF.objects.create(status = JOF.NOT_TAKEN, isrush = new_isrush, name = new_name,description = new_description,date = new_date,pegs = new_pegs,summary = new_summary,type = new_type,spiel = new_spiel, client = new_client, artist = None)
            new_JOF.save()
            return HttpResponseRedirect(reverse('joffeed'))
    return render(request, 'joffeed/createJOF.html',{'form':form, 'account':account})