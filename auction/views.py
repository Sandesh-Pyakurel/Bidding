from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader

from .forms import UserSignupForm, UserLoginForm


def home_view(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render(request=request))

def auction_view(request):
    template = loader.get_template('auctions.html')

    return HttpResponse(template.render(request=request))

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    template = loader.get_template('signup_page.html')

    return HttpResponse(template.render({'form': form}, request=request))


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('home')
    else:
        form = UserLoginForm()
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render({'form': form}, request=request))


def logout_view(request):
    logout(request)
    return redirect('login')
