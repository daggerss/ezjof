from asyncio.windows_events import NULL
from cmath import log
from datetime import datetime
import email
import logging
from pickle import FALSE, TRUE
from telnetlib import STATUS
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from .forms import *

from loginapp.models import Account



@login_required    
def jofarchive(request):
    jofs = JOF.objects.all().order_by('-date')
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    
    if account.type=='Client':
        jofs = jofs.filter(client__department = account.department).order_by('date')
        if account.isHead==False:       
            jofs = jofs.filter(client = account).order_by('date')
            
        
        
        
    elif account.type=='Artist':
        if account.isHead==False:
            jofs = jofs.filter(artist = account).order_by('date')

    if request.GET.get('search'):
            search = request.GET.get('search')
            jofs = jofs.filter(name__icontains = search)   

    return render(request, 'joffeed/archivedJOFs.html', {"jofs":jofs, "account":account})

@login_required
def jofcurrent(request):
    jofs = JOF.objects.filter(~Q(status = 4))
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    
    
    if account.type=='Client':
        jofs = jofs.filter(client__department = account.department).order_by('date')
        if account.isHead==False:       
            jofs = jofs.filter(client = account).order_by('date')
            
        
        
        
    elif account.type=='Artist':
        if account.isHead==False:
            jofs = jofs.filter(artist = account).order_by('date')

    if request.GET.get('search'):
            search = request.GET.get('search')
            jofs = jofs.filter(name__icontains = search)   
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
    return render(request, 'joffeed/settingsJOF.html', {"account":account})

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
    jofs = JOF.objects.filter(status = JOF.NOT_TAKEN).order_by('date')
    return render(request, 'joffeed/JOFfeed.html', {"jofs":jofs, "account":account})

@login_required
def jofapprove(request, pk):
    jof = JOF.objects.get(id = pk)
    jof.isrush = False
    jof.status = JOF.NOT_TAKEN
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    jof.save()
    jofs = JOF.objects.filter(status = JOF.NOT_TAKEN).order_by('date')
    return render(request, 'joffeed/JOFfeed.html', {"jofs":jofs, "account":account})

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
            new_department = new_client.department
            new_JOF = JOF.objects.create(status = JOF.NOT_TAKEN, isrush = new_isrush, name = new_name,description = new_description,date = new_date,pegs = new_pegs,summary = new_summary,type = new_type,spiel = new_spiel, client = new_client, department = new_department, artist = None)
            new_JOF.save()
            return HttpResponseRedirect(reverse('jofcurrent'))
    return render(request, 'joffeed/createJOF.html',{'form':form, 'account':account})

@login_required
def joftracker(request, pk):
    jof = JOF.objects.get(id=pk)
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    comments = Comment.objects.filter(jof = jof)
    if account.type=='Client':
        if jof.status == 3:
            status = 'Not Taken'
            draft = NULL
        if jof.status == 1 or jof.status == 2:
            status = 'In Progress'
            if Draft.objects.filter(jof = jof).exists():
                draft = Draft.objects.filter(jof = jof)
            else:
                draft = NULL
        return render(request, 'joffeed/JOFtracker.html', {"jof":jof, "account":account,"draft":draft,"status":status,"comments":comments})
    elif account.type=='Artist':
        status = 'Is Pending'
        draft = NULL
        form=DraftForm
        comments = Comment.objects.filter(jof = jof)
        if request.method=='POST':      
            form = DraftForm(request.POST)
            if form.is_valid():
                new_file = form.cleaned_data['file']
                jof.spiel = request.POST.get('spiel')
                new_draft = Draft.objects.create(jof=jof, file = new_file)
                new_draft.save()
        return render(request, 'joffeed/JOFtracker.html', {"jof":jof, "account":account,"draft":draft,"status":status,"comments":comments,"form":form})

@login_required
def commentadd(request, pk):
    jof = JOF.objects.get(id=pk)
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    if request.method == "POST":
        content = request.POST.get('commentinput')
        comment = Comment.objects.create(jof=jof, commenter=account, date=datetime.today(),content=content)
        comment.save()
    return redirect('joftracker', pk)