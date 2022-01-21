from django.urls import path
from . import views

app_name = 'choiStory'
urlpatterns = [
    path('', views.main, name='main'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
]