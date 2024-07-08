
from django.urls import path
from . import views

urlpatterns = [

    path('musician_form/',views.form_musician,name='form_musician'),
    path("delete/<int:id>",views.delete_item,name='delete_item'),
    path("edit_musician/<int:id>",views.edit,name='edit')
  

]
