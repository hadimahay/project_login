from .views import Comment,Board
from django.urls import path

app_name = "comment"

urlpatterns = [
    path('',Comment,name="comment"),
    path('bord/',Board, name='board'),
    
]