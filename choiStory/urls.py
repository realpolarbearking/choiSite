from django.urls import path
from . import views

app_name = 'choiStory'
urlpatterns = [
    path('', views.main, name='main'),
    path('resume/', views.aboutMe, name='resume'),
    path('myProjects/', views.myProjects, name='myProjects'),
    path('contactMe/', views.contactMe, name='contactMe'),
]