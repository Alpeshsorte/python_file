from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Question


def home(request):
    # if not request.user.is_authenticated:
    #     return redirect('ragister') 
    # else:
    #     return render('home.html')
    return render(request, 'home.html')

def ragister(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, 'password do not match !')
            return render(request, 'ragister.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'email is allready register')
            return render(request, 'ragister.html')
        
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "ragister successfully")
        return redirect('login')

    return render(request, 'ragister.html')

def login(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        user_pass=request.POST.get('password')
        user = authenticate(request, username=user_name, password=user_pass)

        if user is not None:
            auth_login(request, user)
            messages.success(request,"login successfully")
            return redirect('quiz')
        else:
            messages.error(request, "invalid username and password")
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "user logout succeessfully!")
    return redirect('login')



def quiz(request):
    questions = Question.objects.all()

    if request.method == "POST":
        score = 0

        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.answer:
                score += 1

        return render(request, "result.html", {"score": score})

    return render(request, "quiz.html", {"questions": questions})