from django.urls import path


from .views import Signin, Logout

urlpatterns = [
    path('', Signin.as_view()),
    path('logout/', Logout.as_view()),
]
