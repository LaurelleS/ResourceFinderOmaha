from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from events.models import Organization


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)

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
        
        messages.success(request, 'Account created!')
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
            return redirect('signuporgs')
        # check if org name is in use
        if Organization.objects.filter(name=name).exists():
            messages.error(request, 'Organization name is already in use')
            return redirect('signuporgs')
        
        messages.success(request, 'Account created!')
        org = User.objects.create_user(
            username=username,
            email=email,
        )
        Organization.objects.create(
            org=org,
            name=name,
            description=desc,
            email=email,
            phone=phone
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