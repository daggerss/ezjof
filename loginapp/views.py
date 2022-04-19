from ast import IsNot
import email
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from pyexpat.errors import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from joffeedapp.models import JOF


# Create your views here.
def jofcurrent(request):
    jofs = JOF.objects.all()
    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})
 
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            logemail = form.cleaned_data['email']
            logpass = form.cleaned_data['password']
            user = authenticate(request, username = logemail, password = logpass)
            if user is not None:
                user_login(request, user)
                account = Account.objects.get(email = logemail)
                if account.password == logpass:
                    jofs = JOF.objects.all()
                    return render(request, 'joffeed/currentJOFs.html', {"jofs":jofs})
                else:
                    messages.info(request, 'Email or Password is incorrect')
                

           
    form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def signup(request):
    departments = Department.objects.all().order_by('dname')
    return render(request, 'login/signup.html', {'departments':departments})

def signup_save(request):
    if request.method!='POST':
        return HttpResponseRedirect(reverse('signup'))
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        type = request.POST.get('accounttype')
        department = Department.objects.get(id = request.POST.get('department_id'))
        try:
            user = User.objects.create_user(username = email,
                                 email=email,
                                 password=password)
            account = Account.objects.create(name = name, email = email, password = password, type = type, department = department)
            account.save()
            return HttpResponseRedirect(reverse('jofcurrent'))
        except:
            messages.error(request, 'Username or Email already Exists')
            return HttpResponseRedirect(reverse('signup'))
