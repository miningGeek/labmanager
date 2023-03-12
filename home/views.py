import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

from .utils import quotes
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home_app:home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'home/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_app:login')


@login_required(login_url='home_app:login')
def home(request):
    return render(request, 'home.html')


def index(request):
    length = len(quotes)
    rand_quote = random.randint(0,length)
    quote = quotes[rand_quote-1]
    context = {
        'quote': quote,
    }
    return render(request, 'home/home.html', context)
