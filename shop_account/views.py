from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import LoginForms, RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForms(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('username', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')
    context = {
        'register_form': register_form
    }

    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')




