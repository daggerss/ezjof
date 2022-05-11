from django.urls import path, reverse
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('joffeed', joffeed, name = 'joffeed'),
    path('jofcurrent', jofcurrent, name = 'jofcurrent'),
    path('jofrush', jofrush, name = 'jofrush'),
    path('jofarchive', jofarchive, name = 'jofarchive'),
    path('jofsettings', jofsettings, name = 'jofsettings'),
    path('jofview/<int:pk>', jofview, name = 'jofview'),
    path('jofcreate', jofcreate, name = 'jofcreate'),
    path('jofaccept/<int:pk>', jofaccept, name = 'jofaccept'),
    path('jofapprove/<int:pk>', jofapprove, name = 'jofapprove'),
    
] 
