from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Render the home page of the GCTU web application.
    """
    return render(request, 'gctu_web_app/index.html')