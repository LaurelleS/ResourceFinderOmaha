from django.shortcuts import redirect, render

def login(request):
    if request.method == 'GET':
        return render(request, 'events/templates/home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')