from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework.views import APIView
from ..serializers import CreateAccountSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CreateAccountView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        creds = CreateAccountSerializer(data=request.data)

        if creds.is_valid():
            creds.save()
            print('USER', creds.data)
            user = User.objects.filter(username=creds.username).exists()

            if user:
                return Response(status=401)

            user = User.objects.create_user(**request.data)

            return Response({"token": jwt_encode_handler(
                jwt_payload_handler(user)
            )})
