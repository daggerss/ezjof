from django.urls import path, reverse
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('joffeed', joffeed, name = 'joffeed'),
    path('jofcurrent', jofcurrent, name = 'jofcurrent'),
    path('jofrush', jofrush, name = 'jofrush'),
    path('jofarchive', jofarchive, name = 'jofarchive'),
    path('jofcreate', jofcreate, name = 'jofcreate'),
    path('jofaccept/<int:pk>', jofaccept, name = 'jofaccept'),
    path('jofapprove/<int:pk>', jofapprove, name = 'jofapprove'),
    path('joftracker/<int:pk>', joftracker, name = 'joftracker'),
    path('commentadd/<int:pk>', commentadd, name = 'commentadd'),
    path('draftupload/<int:pk>', draftupload, name = 'draftupload'),
    path('joffinish/<int:pk>', joffinish, name = 'joffinish'),
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)