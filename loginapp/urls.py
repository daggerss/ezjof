from django.urls import path, reverse
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('', login, name='login'),

    path('signup', signup, name='signup'),

    path('signup_save', signup_save, name ='signup_save'),

    path('home/', home, name='home')
] 
