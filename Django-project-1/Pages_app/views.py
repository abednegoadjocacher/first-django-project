from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.
  

def index(request):
    return render(request, 'Pages_app/index.html')
    # return HttpResponse("<h1> Hi welcome </h1>") this is to test whether my function is working .


def contact(request):
    return render(request, 'Pages_app/contact.html')
   # return HttpResponse("<h1> Hi contact me </h1>")

                 
def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'Pages_app/blog.html', {'posts': posts},) #type: ignore
   # return HttpResponse("<h1> Hi lets blog </h1>")