from django import forms

from musican_app import models


class Musician_Form (forms.ModelForm):
    class Meta:
        model = models.musican
        fields = '__all__'