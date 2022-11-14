from artists.models import Artist
from django.db import models
from model_utils.models import TimeStampedModel
from django.core.validators import FileExtensionValidator

# Create your models here.


class Album(TimeStampedModel):

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        default='New Album',
        max_length=200,
        blank=True,
    )

    release_datetime = models.DateField(
        blank=False,
        null=False,
    )
    cost = models.FloatField(
        blank=False,
        null=False,
    )
    is_approved = models.BooleanField(
        blank=True,
        default=False,
    )

    def save(self):
        super().save()
        self.upadetecount()

    def upadetecount(self):

        self.artist.approved_albums = self.artist.album_set.filter(
            is_approved=True).count()
        self.artist.save()

    def __str__(self):
        return self.name


class Song(models.Model):

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=200,
        default=album.name,
        blank=True
    )

    song_img = models.ImageField(
        upload_to='static/albums/data/images',
        blank=False,
        null=False,
    )
    thumbnail = models.ImageField(upload_to='static/albums/data/thumbs')
    song_file = models.FileField(
        upload_to='static/albums/data/media',
        blank=False,
        null=False,
        validators=[FileExtensionValidator(['mp3', 'wav'])],
    )

    url = models.URLField(
        blank=True,

    )

    def delete(self):
        nb = self.album.song_set.all().count()
        print(nb)
        if nb > 1:
            super(Song, self).delete()

    def __str__(self):
        return self.name
