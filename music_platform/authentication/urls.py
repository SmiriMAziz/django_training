from django.urls import path


from .views import Register, UserDetail, Login
from knox import views as knox_views

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
]
