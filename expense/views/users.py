from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Profile
from ..serializers import ProfileSerializer
from rest_framework import permissions


class UserViewset(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserDetail(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
