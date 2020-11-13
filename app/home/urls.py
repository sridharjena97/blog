"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'), #landing page url
    path('contacts/', views.contact, name='contact'), #Endpoint for contact page
    path('about/', views.about, name='about'), #Endpoint for about page
    path('search/', views.search, name='search'), #Endpoint for search page
    path('signup/', views.handleSignup, name='handleSignup'), #Endpoint for signup API
    path('login/', views.handleLogin, name='handleLogin'), #Endpoint for login API
    path('logout/', views.handleLogout, name='handleLogout'), #Endpoint for logout API
]
