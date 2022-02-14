from django.shortcuts import get_object_or_404, render
from .models import blog
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# Create your views here.
def main(request):
    return render(request, 'choiStory/main.html')

def aboutMe(request):
    return render(request, 'choiStory/aboutMe.html')

def myProjects(request):
    posts = blog.objects.all()
    return render(request, 'choiStory/myProjects.html', {'posts': posts})

def contactMe(request):
    return render(request, 'choiStory/contactMe.html')