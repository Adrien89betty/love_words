from django.shortcuts import render

def index(request):
    """Home page."""
    return render(request, 'main_app/index.html')
