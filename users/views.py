from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

def enter_or_registration(request):
    form1 = UserLoginForm()
    form2 = UserRegistrationForm()

    if request.method == 'POST':
        form1 = UserLoginForm(data=request.POST)
        if form1.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form1 = UserLoginForm()

    if request.method == 'POST':
        form2 = UserRegistrationForm(data=request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('users:enter_or_registration'))
    context = {'form1': form1, 'form2': form2}
    return render(request, 'users/enter_or_registration.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Мой профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))