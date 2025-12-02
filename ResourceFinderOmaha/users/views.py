from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from events.models import Organization


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
            return redirect('/home/')
    
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
        group = Group.objects.get(name='Finders')
        group.user_set.add(user)
        return redirect('login')
    
def signuporgs(request):
    if request.method == 'POST':
        # get org info
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # check if username is in use 
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User name is already in use')
            return redirect('signup')
        # check if org name is in use
        if Organization.objects.filter(name=name).exists():
            messages.error(request, 'Organization name is already in use')
            return redirect('signup')
        
        org = User.objects.create_user(
            username=username,
            email=email,
        )
        org.set_password(password)
        org.save()
        group = Group.objects.get(name='Organizations')
        group.user_set.add(org)
        return redirect('login')
    return render(request, 'signuporgs.html')

def logout_view(request):
    logout(request)
    return redirect('login')