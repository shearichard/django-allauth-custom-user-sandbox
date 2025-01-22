from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'
    
def home_page_view2(request): 
    return render(request, 'pages/home.html')

def home_page_view3(request):
    return HttpResponse('Hello World')
