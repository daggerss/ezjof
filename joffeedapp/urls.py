from django.urls import path, reverse
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('joffeed', joffeed, name = 'joffeed'),
    path('jofview', jofview, name = 'jofview'),
    path('jofcurrent', jofcurrent, name = 'jofcurrent'),
    path('jofrush', jofrush, name = 'jofrush'),
    path('jofarchive', jofarchive, name = 'jofarchive'),
    path('jofsettings', jofsettings, name = 'jofsettings')
] 
