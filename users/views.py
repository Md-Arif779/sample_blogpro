from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, Your account was successfully')
            return redirect('home')
    else:
            form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form}) 

@login_required
def profile(request):
                           
     return render(request, 'users/profile.html')    

@login_required
def profile_update(request):
     if request.method == "POST":
         u_form = UserUpdateForm(request.POST, instance=request.user)
         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
         if u_form.is_valid() and p_form.is_valid():
              u_form.save()
              p_form.save()
     else:
          u_form = UserUpdateForm(instance=request.user)
          p_form = ProfileUpdateForm(instance=request.user.profile)
     context ={
              'u_form': u_form,
              'p_form': p_form   
               } 
     success_url = reverse_lazy('home')                                   
     return render(request, 'users/profile_update.html', context)    

     
















