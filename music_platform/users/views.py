from django.http import Http404
from rest_framework.response import Response
from users.models import User
from authentication.serializer import UserDetailedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework import status

# Create your views here.


class UserDetail(APIView):

    authentication_classes = [TokenAuthentication,
                              SessionAuthentication, BasicAuthentication]

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio,
                "password": user.password
            }

        })

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserDetailedSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserDetailedSerializer(
            snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
