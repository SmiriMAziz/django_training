from django import forms
from artists.models import Artist
from django.forms import ValidationError


def validate_album(Album):
    print(Album.song_set.all().count())
    if Album.song_set.all().count() < 1:
        raise ValidationError('no song error')


class AlbumForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    name = forms.CharField(max_length=200)
    release_datetime = forms.DateField(widget=forms.SelectDateWidget)
    cost = forms.FloatField()
    validators = [validate_album]
