from artists.models import Artist
from django.db import models

# Create your models here.


class Album(models.Model):

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        default='New Album',
        max_length=200,
        blank=True,
    )
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(
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
