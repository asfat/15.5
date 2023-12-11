from django import forms
from . import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model= models.Album
        fields='__all__'
        exclude=['release_date']
        labels={
            'albumName': 'Album Name',
        }
        widgets={
            'release_date':forms.DateInput(attrs={'type':'date'})
        }
        help_text={
            'rating':'Choose any number from 0 to 5',
        }
