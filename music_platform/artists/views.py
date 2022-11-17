from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404
from .forms import ArtistForm
from .models import Artist
from django.views.generic import TemplateView
from albums.models import Album
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from artists.models import Artist
from .serializers import ArtistSerializer
from rest_framework.views import APIView


class CreateArtist(APIView):

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
        return Response()


class GenerateArtists(APIView):

    def get(self, request, format=None):
        aritsts = Artist.objects.all()
        serializer = ArtistSerializer(aritsts, many=True)
        return Response(serializer.data)
