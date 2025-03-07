from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

# Create your views here.

#------------------- index page ----------------#

def index(request):
    return render(request, 'index.html')

#----------- user registration page -------------#

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
        
        else:
            errors = form.errors
            return render(request, 'register.html', {'form': form, 'errors': errors})
            

    form = UserRegisterForm()
    context = {'form': form}

    return render(request, 'register.html', context=context)


#----------- user login page -------------#

def login(request):
    if request.method == 'POST':
        print('post request ok')
        form = UserLoginForm(request, data = request.POST)

        if form.is_valid():
            print('form validation ok')
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('home')
            
        else:
            return render(request, 'login.html', {'form': form})
        

    form = UserLoginForm()

    context = {'form': form}

    return render(request, 'login.html', context=context)


#---------------- user logout -------------#

def logout(request):
    auth.logout(request)

    return redirect('')


#---------------- home page --------------#

def home(request):
    return render(request, 'home.html')
