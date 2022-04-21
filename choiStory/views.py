from django.shortcuts import get_object_or_404, render
from .models import blog
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.core.mail import send_mail

# Create your views here.
def main(request):
    return render(request, 'choiStory/main.html')

def aboutMe(request):
    return render(request, 'choiStory/aboutMe.html')

def myProjects(request):
    posts = blog.objects.all()
    return render(request, 'choiStory/myProjects.html', {'posts': posts})

def contactMe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        msg = request.POST.get("msg")
        data = {
            "Name" : name ,
            "E-MAIL" : email,
            "Subject" : subject,
            "Message" : msg
        }
        message = '''
        New message: {}
        
        From: {}
        '''.format(data["Message"], data["E-MAIL"])
        send_mail(data["Subject"], message, '', ["kk6962289@gmail.com"])
        return HttpResponse('Your message has been sent. Thank you.')

    return render(request, 'choiStory/contactMe.html', {})

# def contactMe(request):
#     return render(request, 'choiStory/contactMe.html')

def post_detail(request, id):
	post = get_object_or_404(blog, id=id)
	return render(request, 'choiStory/post_detail.html', {"post": post})