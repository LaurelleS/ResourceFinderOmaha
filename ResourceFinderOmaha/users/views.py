from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

         # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home')
    
    return render(request, 'login.html')



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        # get user info
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User name is already in use')
            return redirect('/signup/')
        
        user = User.objects.create_user(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return redirect('login')