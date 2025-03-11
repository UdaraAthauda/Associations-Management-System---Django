from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#------------------- index page ----------------#

def index(request):
    return render(request, 'index.html')


#------------------ about us page --------------------#

@login_required(login_url='login')
def aboutUs(requets):
    return render(requets, 'aboutUs.html')


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

@login_required(login_url='login')
def home(request):

    user = request.user
    members = AssociationMember.objects.filter(adminAccept=True, user=user)
    notReg = Association.objects.exclude(members__in=members)

    context = {'associations': notReg }

    return render(request, 'home.html', context=context)


#---------------- association details display -----------------#

@login_required(login_url='login')
def associationDetails(request, pk):
    association = Association.objects.get(id=pk)

    context = {'association': association}

    return render(request, 'userTemplates/associationDetails.html', context=context)


#------------------- membership request process ----------------------#

@login_required(login_url='login')
def membershipRequest(request, pk):
    try:
        association = Association.objects.get(id=pk)
        user = request.user

        if association and user is not None:
            AssociationMember.objects.create(user=user, association=association)
            messages.success(request, 'Request is successfully submitted!')
            return redirect(reverse('associationDetails', kwargs={'pk': pk}))
    except:
        messages.error(request, 'Request is already submitted, or error in the process?')
        return redirect(reverse('associationDetails', kwargs={'pk': pk}))
    
    
#-------------------- membership display ----------------------#

@login_required(login_url='login')
def memberships(request):
    currentUser = request.user
    members = AssociationMember.objects.filter(adminAccept=True, user=currentUser)
    registered = Association.objects.filter(members__in=members)

    context = {'associations': registered}

    return render(request, 'userTemplates/memberships.html', context=context)


#------------------- association services display --------------------#

@login_required(login_url='login')
def services(request, pk):
    association = Association.objects.get(id=pk)
    services = Service.objects.filter(association=association)
    associationName = association.AssociationName
    
    context = {'services': services, 'associationName':associationName}

    return render(request, 'userTemplates/services.html', context=context)


#------------------- association service request process ----------------------#

@login_required(login_url='login')
def serviceRequest(request, pk):    
    try:
        service = Service.objects.get(id=pk)

        association = Association.objects.filter(services=service)
        for a in association:
            id = a.id

        user = request.user

        if service and user is not None:
            ServiceRequest.objects.create(user=user, service=service)
            messages.success(request, 'Request is successfully submitted!')
            return redirect(reverse('services', kwargs={'pk': id}))
    except:
        messages.error(request, 'Request is already submitted, or error in the process?')
        return redirect(reverse('services', kwargs={'pk': id}))


#-------------------- user profile/update --------------------#

@login_required(login_url='login')
def userProfile(request):
    currentUser = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=currentUser)

        if form.is_valid():
            form.save()
            return redirect('userProfile')
        
        else:
            errors = form.errors
            return render(request, 'userTemplates/userProfile.html', {'form': form, 'errors': errors})


    form = UserUpdateForm(instance=currentUser)

    context = {'form': form}

    return render(request, 'userTemplates/userProfile.html', context=context)


#-------------------- user password change -------------------------#

@login_required(login_url='login')
def password(request):
    currentUser = request.user

    if request.method == 'POST':
        form = PasswordChangeForm(currentUser, request.POST)

        if form.is_valid():
            form.save()

            return redirect('logout')
        
        else:
            return render(request, 'userTemplates/passwordChange.html', context={'form': form})
        
    form = PasswordChangeForm(currentUser)

    context = {'form': form}

    return render(request, 'userTemplates/passwordChange.html', context=context)


#----------------------- user feedbacks --------------------#

@login_required(login_url='login')
def feedbacks(request):
    currentUser = request.user

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            addUser = form.save(commit=False)
            addUser.user = currentUser
            addUser.save()
            messages.success(request, 'Feedback is successfully submitted!')
            return redirect('feedbacks')
        else:
            messages.error(request, 'There is an error in the process?')
            return render(request, 'userTemplates/feedbacks.html', context={'form': form})

    form = FeedbackForm()

    context = {'form': form}

    return render(request, 'userTemplates/feedbacks.html', context=context)

