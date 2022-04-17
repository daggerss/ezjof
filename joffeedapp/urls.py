from django.urls import path, reverse
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('jofcurrent', jofcurrent, name = 'jofcurrent'),
    path('jofrush', jofrush, name = 'jofrush'),
    path('jofpending', jofpending, name = 'jofpending'),
    path('jofarchive', jofarchive, name = 'jofarchive'),
    path('jofsettings', jofsettings, name = 'jofsettings')
] 
