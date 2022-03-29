from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login,logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group

# from .forms import RegistrationForm

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard/')
        else:
            messages.info(request,"Username or Password is incorrect")

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def forget_password(request):
    return render(request,'Forget_password.html')

def userPage(request):
    return HttpResponse("you are on user page")

@login_required(login_url="login")
def logoutuser(request):
    logout(request)
    messages.info(request,"Successfully Logout.")
    return redirect('login')

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request,'Profile is created for '+username)
            return redirect('login')
    return render(request,'signup.html',{'form':form})


@unauthenticated_user
def agency_signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Admin')
            user.groups.add(group)

            messages.success(request,'Profile is created for '+username)
            return redirect('login')
    return render(request,'agency_signup.html',{'form':form})