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
        jofs = jofs.filter(client__department = account.department).order_by('status')
        if account.isHead==False:       
            jofs = jofs.filter(client = account).order_by('status')
            
        
        
        
    elif account.type=='Artist':
        if account.isHead==False:
            jofs = jofs.filter(artist = account).order_by('-status')

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
    comments = Comment.objects.filter(draft__jof = jof)
    drafts = Draft.objects.filter(jof = jof)

    return render(request, 'joffeed/JOFtracker.html', {"jof":jof, "account":account,"comments":comments, "drafts":drafts})

@login_required
def commentadd(request, pk):
    draft = Draft.objects.get(id=pk)
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    if request.method == "POST":
        content = request.POST.get('commentinput')
        comment = Comment.objects.create(draft=draft, commenter=account, date=datetime.today(),content=content)
        comment.save()
        dcount = Draft.objects.filter(jof = draft.jof).count()
        if(dcount<3 and draft.jof.status!=4):
            draft.jof.status = 2
            draft.jof.save()
    return redirect('joftracker', draft.jof.id)

@login_required
def draftupload(request, pk):
    jof = JOF.objects.get(id=pk)
    current_user = request.user
    account = Account.objects.get(email = current_user.username)
    
    dnum = Draft.objects.filter(jof = jof).count() + 1
    if request.method == "POST":
        spiel = request.POST.get('spielinput')
        file = request.FILES.get('fileinput')
        draft = Draft.objects.create(jof=jof, spiel=spiel, dnum = dnum, file=file)
        draft.save()
        jof.status = 1
        jof.save()
    return redirect('joftracker', pk)

@login_required
def joffinish(request, pk):
    jof = JOF.objects.get(id=pk)
    jof.status = 4
    jof.save()  
    return redirect('joftracker', pk)