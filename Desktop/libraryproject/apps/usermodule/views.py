from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate, login

def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # encrypt
            user.save()
            messages.success(request, "You have successfully registered.")
            return redirect('login')  
    else:
        form = SignUpForm()
    return render(request, 'usermodule/register.html', {'form': form})




def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'usermodule/login.html', {'form': form})


def homePage(request):
    return render(request, 'usermodule/home.html')

from django.contrib.auth import logout

def logoutUser(request):
    logout(request)
    messages.info(request, "You have been logged out.") 
    return redirect('login')
