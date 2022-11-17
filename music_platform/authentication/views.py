from django.contrib.auth import login, logout
from knox.views import LogoutView as KnoxLogoutView
from django.http import Http404
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from users.models import User
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from django.contrib.auth.hashers import make_password
# Create your views here.


class Register(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            [username, email, password, bio] = [serializer.data['username'],
                                                serializer.data['email'], serializer.data['password'], serializer.data['bio']]
            user = User(username=username, email=email,
                        password=make_password(password), bio=bio)
            user.save()
            token = Token.objects.create(user=user)
            return Response(serializer.data)
        return Response(serializer.errors)


class Login(KnoxLoginView):

    def post(self, request, *args, **kwargs):

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'token': token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio,


            }

        })


class Logout(KnoxLogoutView):

    authentication_classes = [TokenAuthentication,
                              SessionAuthentication, BasicAuthentication]

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)

        return Response('User Logged out successfully')
