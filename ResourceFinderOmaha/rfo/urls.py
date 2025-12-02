"""
URL configuration for rfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from users import views as user_views
from events import views as event_views

urlpatterns = [
    # automatically bring user to login page
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # include django views and routes (account/login etc..)
    path('signup/', user_views.signup, name='signup'),
    path('accounts/profile/', event_views.home, name='home'),
    path('signuporgs/', user_views.signuporgs, name='signuporgs'),

    path('eventdetail/<int:event_id>/', event_views.eventDetail, name='eventDetail'),
    path('myevents/', event_views.myevents, name='myevents'),
     path('viewevent/<int:event_id>/', event_views.viewEvent, name='viewEvent'),
    path('logout/', user_views.logout_view, name='logout'),
]
