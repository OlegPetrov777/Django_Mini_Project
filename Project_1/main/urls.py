from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create_new', views.create, name='create'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
]