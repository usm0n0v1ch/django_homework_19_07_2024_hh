from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def register(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('resume_list')
        return redirect('vacancy_list')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vacancy_list')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('resume_list')
        return redirect('vacancy_list')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                return redirect('register')
            login(request, user)
            if request.user.is_staff:
                return redirect('resume_list')
            return redirect('vacancy_list')

    form = LoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)

def log_out(request):
    logout(request)
    return redirect('login')
