from django.shortcuts import render

def index(request):
    return render(request, 'Main/index.html')

def contact(request):
    return render(request, 'Main/contact.html')

def graphisme(request):
    return render(request, 'Main/portfolio_graphisme.html')
