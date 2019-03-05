from rest_framework import serializers
from django.contrib.auth.models import User


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
