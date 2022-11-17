from rest_framework import serializers
from rest_framework.serializers import ValidationError
from users.models import User


def validate_email(email):
    if User.objects.filter(email=email).count() > 0:
        raise ValidationError('email already exists')
    return email


def validate_username(username):
    if User.objects.filter(username=username).count() > 0:
        raise ValidationError('username already exists')
    return username


def hash(passowrd):
    hash_value = 0
    p = 29
    mod = 1e9+7
    for c in passowrd:
        hash_value = (hash_value + ord(c)*p) % mod
        p = (p*29) % mod
    return hash_value


def validate_password_strong(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    return hash(password)


def validate_password(self):
    if self['password'] != self['confirm_password']:
        raise ValidationError("confirmation password don't match")
    return self['password']


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(validators=[validate_username])
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(
        validators=[validate_password_strong], required=True)
    confirm_password = serializers.CharField(
        validators=[validate_password_strong], required=True)
    bio = serializers.CharField(max_length=256, required=False)

    class Meta():
        model = User
        fields = ['username', 'email', 'password', 'confirm_password',  'bio']
        validators = [validate_password]


class UserDetailedSerializer(serializers.ModelSerializer):

    username = serializers.CharField(validators=[validate_username])
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(
        validators=[validate_password_strong], required=True)
    bio = serializers.CharField(max_length=256, required=False)

    class Meta():
        model = User
        fields = ['username', 'email', 'password', 'bio']
