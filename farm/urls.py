from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('',  views.index,name='home'),
     path('project',  views.project , name = 'project'),
      path('reminder',  views.reminder, name ='reminder'),
      path('accounts',  views.accounts, name = 'accounts'),
      path('profile',  views.profile, name = 'profile'),
      
       path('evaluate',  views.evaluate, name = 'evaluate'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
