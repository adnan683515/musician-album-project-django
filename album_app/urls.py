
from django.urls import path
from . import views

urlpatterns = [

    path('',views.album,name='album_page'),
    path("edit/<int:id>",views.edit_album,name='edit_page'),
    path("album_form/",views.albumform,name='album_form'),
    
    # path("register/",views.registerform,name='register'),
    path("register/",views.register.as_view(),name='register'),
    
    path("login/",views.log_in,name='log_in'),
    path('logout/',views.log_out,name='log_out')

  
    
]