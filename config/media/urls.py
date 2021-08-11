from config.media.views import media_example
from django.urls import path 

urlpatterns = [
    path('',media_example,name='media'), 
    
]
