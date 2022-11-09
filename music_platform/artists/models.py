from django.db import models

# Create your models here.


class Artist(models.Model):
    Stage_name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        unique=True,
    )
    social_link = models.URLField(
        blank=False,
        null=False,
    )
    approved_albums = models.IntegerField(
        default=0,
        blank=True,
    )

    def __str__(self):
        return self.Stage_name

    class Meta:
        ordering = ['Stage_name']
