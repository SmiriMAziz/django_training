from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404
from .forms import ArtistForm
from .models import Artist
from django.views.generic import TemplateView
from albums.models import Album
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateArtist(LoginRequiredMixin, TemplateView):

    login_url = '/signin/'
    redirect_field_name = 'artists'
    initial = {'key': 'value'}
    form = ArtistForm
    template_name = 'artists.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():

            stage_name = form.cleaned_data['stage_name']
            social_link = form.cleaned_data['social_link']
            if (Artist.objects.filter(Stage_name=stage_name).count() > 0):
                return render(request, 'errors.html')

            else:
                a = Artist(Stage_name=stage_name, social_link=social_link)
                a.save()

            return HttpResponseRedirect('/admin/')


class GenerateArtists(TemplateView):

    initial = {'key': 'value'}
    template_name = 'allartists.html'

    def get(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        albums = Album.objects.all()
        return render(request, self.template_name, {'albums': albums, 'artists': artists})
