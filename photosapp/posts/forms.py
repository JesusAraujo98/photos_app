from django import forms

class AlbumForm(forms.Form):
    album_client = forms.CharField(label= 'Cliente', max_length=200, required=True)
    album_name = forms.CharField(label= 'titulo', max_length=100, required=True)
    cover_photo = forms.ImageField()

