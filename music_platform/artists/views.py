from .models import Artist
from rest_framework.response import Response
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
