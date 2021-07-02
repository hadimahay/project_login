from .views import sinup , profile
from django.urls import path,include

app_name = "Sin"

urlpatterns = [
    path('',include('django.contrib.auth.urls'),name="login"),
    path('sinup', sinup ,name='Sinup'),
    path('profile/', profile, name='profile')
    
]