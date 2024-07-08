from django import forms
from album_app.models import Album


class album_form(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"