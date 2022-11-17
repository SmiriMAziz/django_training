from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(
        max_length=256,
        blank=True,
        # widget=forms.Textarea,
    )
