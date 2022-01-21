from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# Create your views here.
def main(request):
    return render(request, 'choiStory/main.html')

def aboutMe(request):
    return render(request, 'choiStory/aboutMe.html')
