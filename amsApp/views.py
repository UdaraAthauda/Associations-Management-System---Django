from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

#------------------- index page ----------------#

def index(request):
    return render(request, 'index.html')

#----------- user registration page -------------#

def register(request):

    if request.method == 'POST':
        print('post request ok')
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            print('form validation ok')
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
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
