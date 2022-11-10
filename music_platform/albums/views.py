from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AlbumForm
from .models import Album


def create_album(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST)

        # check whether it's valid:
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
                print('ok')

            return HttpResponseRedirect('/admin/')

    else:
        form = AlbumForm()

    return render(request, 'albums.html', {'form': form})
