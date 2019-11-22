from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, 'index.html')

def group(request):
  return render(request, 'group.html')

def festival(request):
  return render(request, 'festival.html')