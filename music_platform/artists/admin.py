from albums.models import Album
from django.contrib import admin
from .models import Artist
# Register your models here.


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 0


@admin.register(Artist)
class Show(admin.ModelAdmin):
    list_display = ('Stage_name', 'approved_albums')
    inlines = [
        AlbumInline,
    ]
