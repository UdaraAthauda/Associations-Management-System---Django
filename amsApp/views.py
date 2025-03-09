from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages

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

    user = request.user
    members = AssociationMember.objects.filter(adminAccept=True, user=user)
    notReg = Association.objects.exclude(members__in=members)

    context = {'associations': notReg }

    return render(request, 'home.html', context=context)


#---------------- association details display -----------------#

def associationDetails(request, pk):
    association = Association.objects.get(id=pk)

    context = {'association': association}

    return render(request, 'userTemplates/associationDetails.html', context=context)


#------------------- membership request process ----------------------#

def membershipRequest(request, pk):
    try:
        association = Association.objects.get(id=pk)
        user = request.user

        if association and user is not None:
            AssociationMember.objects.create(user=user, association=association)
            messages.success(request, 'Request is successfully submitted')
            return redirect(reverse('associationDetails', kwargs={'pk': pk}))
    except:
        messages.error(request, 'Request is already submitted, or error in the process?')
        return redirect(reverse('associationDetails', kwargs={'pk': pk}))
    
    
#-------------------- membership display ----------------------#

def memberships(request):
    currentUser = request.user
    members = AssociationMember.objects.filter(adminAccept=True, user=currentUser)
    registered = Association.objects.filter(members__in=members)

    context = {'associations': registered}

    return render(request, 'userTemplates/memberships.html', context=context)


#------------------- association services display --------------------#

def services(request, pk):
    association = Association.objects.get(id=pk)
    services = Service.objects.filter(association=association)
    associationName = association.AssociationName
    
    context = {'services': services, 'associationName':associationName}

    return render(request, 'userTemplates/services.html', context=context)


#------------------- association service request process ----------------------#

def serviceRequest(request, pk):    
    try:
        service = Service.objects.get(id=pk)

        association = Association.objects.filter(services=service)
        for a in association:
            id = a.id

        user = request.user

        if service and user is not None:
            ServiceRequest.objects.create(user=user, service=service)
            messages.success(request, 'Request is successfully submitted')
            return redirect(reverse('services', kwargs={'pk': id}))
    except:
        messages.error(request, 'Request is already submitted, or error in the process?')
        return redirect(reverse('services', kwargs={'pk': id}))
