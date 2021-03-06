from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
  if request.method == "POST":
    if request.POST["password1"] == request.POST["password2"]:
      username = request.POST["username"]
      password = request.POST["password"]
      email = request.POST["email"]
      
      user = User.objects.create_user(username, password, email)
      user.save()
      auth.login(user)

      return redirect('/index/')
    return redirect('signup.html')
  return render(request, 'signup.html')

def login(request):
  if request.method =="POST":
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('/index')
    else:
      return redirect('login.html')
  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('/index')


# Create your views here.
