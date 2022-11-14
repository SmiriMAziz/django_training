from django.urls import path

from .views import CreateArtist, GenerateArtists

urlpatterns = [
    path('create/', CreateArtist.as_view()),
    path('', GenerateArtists.as_view()),

]
