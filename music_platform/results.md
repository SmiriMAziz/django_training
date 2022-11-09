from artists.models import Artist
from albums.models import Album
from datetime import datetime

create some artists
artist_1 = Artist(Stage_name = "drake" , social_link = "https://www.instagram.com/drake/")
artist_2 = Artist(Stage_name = "eminem" , social_link = "https://www.instagram.com/eminem/")
artist_3 = Artist(Stage_name = "50cent" , social_link = "https://www.instagram.com/50cent/")
artist_1.save()
artist_2.save()
artist_3.save()

list down all
Artist.objects.all()
<QuerySet [<Artist: 50cent>, <Artist: drake>, <Artist: eminem>]>

list down all artists sorted by name
(they are already sorted by name !)
Artist.objects.all().order_by('Stage_name')
<QuerySet [<Artist: 50cent>, <Artist: drake>, <Artist: eminem>]>

list down all artists whose name starts with a
Artist.objects.filter(Stage_namestartswith='a')
<QuerySet
with e
Artist.objects.filter(Stage_namestartswith='e')
<QuerySet [<Artist: eminem>]>

in 2 different ways, create some albums and assign them to any artists (hint: use objects manager and use the related object reference)
album_1 = Album(artist = artist_2 , name='slim_shady' , release_datetime = datetime(1999, 2, 23, 0, 0, 0), cost = 50)
album_2 = Album(artist = artist_1 , name='nevermind' , release_datetime = datetime(2022, 1, 1, 23,23,23), cost = 150)
album_1.save()
album_2.save()
a = Artist.objects.get(id=4)
print(a)
50cent
album_3 = a.album_set.create(name='nooneknows' , release_datetime = datetime(2023, 12, 24, 12, 12, 12), cost = 250)

get the latest released album
Album.objects.order_by('-release_datetime')[0]
<Album: nooneknows>

get all albums released before today
today = datetime.today().date()
Album.objects.filter(release_datetime\_\_lt=today)
<QuerySet [<Album: slim_shady>, <Album: nevermind>]>

get all albums released today or before but not after today
Album.objects.filter(release_datetime\_\_lte=today)
<QuerySet [<Album: slim_shady>, <Album: nevermind>]>

count the total number of albums (hint: count in an optimized manner)
Album.objects.count()
3

in 2 different ways, for each artist, list down all of his/her albums (hint: use objects manager and use the related object reference)
for artist in Artist.objects.all():
... artist.album_set.all()
...
<QuerySet [<Album: nooneknows>]>
<QuerySet [<Album: nevermind>]>
<QuerySet [<Album: slim_shady>]>
for artist in Artist.objects.all():
... Album.objects.filter(artist=artist)
...
<QuerySet [<Album: nooneknows>]>
<QuerySet [<Album: nevermind>]>
<QuerySet [<Album: slim_shady>]>

list down all albums ordered by cost then by name (cost has the higher priority)
Album.objects.all().order_by('cost','name')
<QuerySet [<Album: slim_shady>, <Album: nevermind>, <Album: nooneknows>]>
