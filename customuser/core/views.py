from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


def signup_confirmation_view(request):
    return render(request, 'signupconfirmation.html')
