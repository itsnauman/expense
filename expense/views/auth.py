from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..serializers import SignUpSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CreateAccountView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(username=serializer.validated_data.get('username')).exists()
        if user:
            return Response({'success': False}, status=status.HTTP_403_FORBIDDEN)

        saved_user = serializer.save()
        jwt_token = jwt_encode_handler(jwt_payload_handler(saved_user))
        return Response({'token': jwt_token}, status=status.HTTP_201_CREATED)
