from django import forms


class ArtistForm(forms.Form):
    stage_name = forms.CharField(max_length=200)
    social_link = forms.URLField()
