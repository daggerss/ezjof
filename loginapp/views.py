import email
from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

# Create your views here.
def home(request):

    return render(request, 'base.html')
 
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            logemail = form.cleaned_data['email']
            logpass = form.cleaned_data['password']
            if Account.objects.filter(email = logemail).exists():
                account = Account.objects.get(email = logemail)
                if account.password == logpass:
                    return render(request, 'base.html')
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
            account = Account.objects.create(name = name, email = email, password = password, type = type, department = department)
            account.save()
            return HttpResponseRedirect(reverse('home'))
        except:
            messages.error(request, 'Username or Email already Exists')
            return HttpResponseRedirect(reverse('signup')) 
