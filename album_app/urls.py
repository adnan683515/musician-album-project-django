
from django.urls import path
from . import views

urlpatterns = [

    path('',views.album,name='album_page'),
    path("edit/<int:id>",views.edit_album,name='edit_page'),
    path("album_form/",views.albumform,name='album_form'),

  
    
]