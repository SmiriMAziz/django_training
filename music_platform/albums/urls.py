from django.urls import path

from .views import CreateAlbum, GenerateImages


urlpatterns = [
    path('create/', CreateAlbum.as_view()),
    path('img/', GenerateImages.as_view()),

]
