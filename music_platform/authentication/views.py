from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
from .serializer import UserSerializer, hash
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.


class Register(APIView):

    print(User.objects.all())

    def post(self, request, *args, **kwargs):

        print(User.objects.all())
        for user in User.objects.all():
            print(user)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            [username, email, password, bio] = [serializer.data['username'],
                                                serializer.data['email'], serializer.data['password'], serializer.data['bio']]
            print([username, email, password, bio])
            user = User(username=username, email=email,
                        password=hash(password), bio=bio)
            user.save()
            token = Token.objects.create(user=user)

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
                "bio": user.bio
            }

        })

        return Response(serializer.errors)

# class Register(TemplateView):
#     initial = {'key': 'value'}
#     form = SigninForm
#     template_name = 'signin.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=email, password=password)
#             if (user is not None):
#                 login(request, user)
#                 return HttpResponseRedirect('/admin')
#             else:
#                 return HttpResponseRedirect('/artists')

#             # return render(request, self.template_name, {'form': form})


# class Logout(TemplateView):

#     def get(self, request, *args, **kwargst):
#         logout(request)
#         return HttpResponseRedirect('/artists')


# class Logout(APIView):

#     print('hello')
#     authentication_classes = [SessionAuthentication,
#                               BasicAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     permission_classes = [IsAuthenticated]

#     # def get(self, request, format=None):
#     #     print(request.user)
#     #     # simply delete the token to force a login

#     #     if request.user is not None:
#     #         request.user.auth_token.delete()
#     #         return Response('ok')
#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)
