from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404
from .forms import ArtistForm
from .models import Artist

from albums.models import Album


def get_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            stage_name = form.cleaned_data['stage_name']
            social_link = form.cleaned_data['social_link']
            if (Artist.objects.filter(Stage_name=stage_name).count() > 0):
                return render(request, 'errors.html')

            else:
                a = Artist(Stage_name=stage_name, social_link=social_link)
                a.save()

            return HttpResponseRedirect('/admin/')

    else:
        form = ArtistForm()

    return render(request, 'artists.html', {'form': form})


def get_all(request):

    artists = Artist.objects.all()
    albums = Album.objects.all()
    return render(request, 'allartists.html', {'albums': albums, 'artists': artists})
