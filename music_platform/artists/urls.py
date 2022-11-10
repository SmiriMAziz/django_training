from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.get_artist),
    path('', views.get_all),

]
