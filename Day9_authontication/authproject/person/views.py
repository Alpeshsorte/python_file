from django.shortcuts import render, redirect
from django.contrib.auth.models import User, 


# Create your views here.

def home(request):

    return render(request, 'home.html')


def login(request):

    return render(request, 'login.html')

def logout(request):

    return render(request, 'logout.html')

def ragister(request):

    return render(request, 'ragister.html')

