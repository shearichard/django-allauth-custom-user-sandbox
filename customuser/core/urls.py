"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import re_path, path, include
from .views import HomePageView, home_page_view2, home_page_view3 

urlpatterns = [
    path('home3/', home_page_view3, name='dacusindex'), 
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
#path('foo/', TemplateView.as_view(template_name='index.html'), name='dacusindexfoo'),
#path('', TemplateView.as_view(template_name='index.html'), name='dacusindex'),
    #re_path(r'^$', TemplateView.as_view(template_name='index.html'), name='dacusindex'),
    #re_path(r'^$', TemplateView.as_view(template_name='index.html'), name='dacusindex'),
    #path('home4/', TemplateView.as_view(template_name='index.html'), name='dacusindex'),
