from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AlbumForm
from .models import Album, Song
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateAlbum(LoginRequiredMixin, TemplateView):

    login_url = '/signin/'
    redirect_field_name = 'artists'
    initial = {'key': 'value'}
    form = AlbumForm
    template_name = 'albums.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            artist = form.cleaned_data['artist']
            name = form.cleaned_data['name']
            release_datetime = form.cleaned_data['release_datetime']
            cost = form.cleaned_data['cost']

            if (Album.objects.filter(name=name).count() > 0):
                return render(request, 'errors.html')

            else:
                album_1 = Album(artist=artist, name=name,
                                release_datetime=release_datetime, cost=cost)
                album_1.save()

            return HttpResponseRedirect('/admin/')


class GenerateImages(TemplateView):

    initial = {'key': 'value'}
    template_name = 'images.html'

    def get(self, request, *args, **kwargs):

        songs = Song.objects.all()
        print(songs)
        for song in songs:
            print(song.song_img)
        return render(request, self.template_name, {'songs': songs})
