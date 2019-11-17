from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm


def login(request):
    title = 'Вход'
    login_form = UserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    context = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def registration(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()

    context = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/registration.html', context)
