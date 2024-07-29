from django import forms
from album_app.models import Album
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class album_form(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
    
class registerModel(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']