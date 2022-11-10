from django import forms
from artists.models import Artist


class AlbumForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    name = forms.CharField(max_length=200)
    release_datetime = forms.DateField(widget=forms.SelectDateWidget)
    cost = forms.FloatField()
