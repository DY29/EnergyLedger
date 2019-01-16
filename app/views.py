from time import timezone

from django.shortcuts import render, get_object_or_404


# Create your views here.
from app.models import Energy


def about(request):
    return render(request, 'app/about.html', {'about':about})

def blog(request):
    return render(request, 'app/blog.html', {'blog': blog})

def blog_single(request):
    return render(request, 'app/blog_single.html', {'blog': blog})

def contact(request):
    return render(request, 'app/contact.html', {'contact': contact})

def index(request):
    return render(request, 'app/index.html', {'index': index})

def portfolio(request):
    return render(request, 'app/portfolio.html', {'portfolio': portfolio})

def services(request):
    return render(request, 'app/services.html', {'services': services})

def support(request):
    return render(request, 'app/support.html', {'support': support})

def technology(request):
    return render(request, 'app/technology.html', {'technology': support})

