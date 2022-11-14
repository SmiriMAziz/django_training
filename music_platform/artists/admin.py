from albums.models import Album
from django.contrib import admin
from .models import Artist
# Register your models here.


@admin.register(Artist)
class Show(admin.ModelAdmin):
    list_display = ('Stage_name', 'approved_albums')
    ordering = ['-approved_albums']
    readonly_fields = ['approved_albums']
