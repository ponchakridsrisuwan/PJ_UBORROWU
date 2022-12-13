"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include # new
from myapp.views import *
from myappstaff.views import *
from myappSuper.views import *
from myapp.models import *
from myappstaff.models import *
from myappSuper.models import *
from django.contrib.auth import views as auth_views
from myproject.settings import AUTHENTICATION_BACKENDS

def login(req):
    if req.method == 'POST':
        user = AUTHENTICATION_BACKENDS
        if user is not AUTHENTICATION_BACKENDS:
            login(req, user)
            return redirect('/')
        else:
            return render(req, 'pages/login.html')
    return render(req, 'pages/login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #accounts/login
    #path('', views.user_index, name='user_index'), 
    path('',include('myapp.urls')),
    path('',include('myappstaff.urls')),
    path('',include('myappSuper.urls')),
    path('login/', login,name='login'),
    #path('login/', auth_views.LoginView.as_view(template_name = 'pages/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'pages/logout.html'),name='logout'),
    
]
