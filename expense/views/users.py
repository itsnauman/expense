from rest_framework.generics import ListAPIView
from ..models import Profile
from ..serializers import ProfileSerializer


class UserViewset(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
