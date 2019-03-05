from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.CharField(required=True, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, write_only=True)

    def create(self, data):
        user = User.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('first_name'),
        )

        user.set_password(data.get('password'))
        user.save()
        return user

    def update(self, user, data):
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.set_password(data.get('password'))
        user.save()

        return user
