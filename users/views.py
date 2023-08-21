from time import sleep

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import CustomUser
from users.permissions import UserProfilePermission
from users.serializers import CodeEnterSerializer, CustomUserInviteSerializer, \
    CustomUserProfileSerializer, PhoneEnterSerializer

from users.services import check_write_invite, generate_code


class PhoneEnterView(APIView):
    """
    Enter phone number. Format +11234567890.
    After follow page /code/
    """

    def post(self, request, **kwargs):
        serializer = PhoneEnterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sleep(2)
        code = generate_code()
        request.session['code'] = code
        request.session['phone'] = serializer.data.get('phone')

        return Response({'Your auth code': code, 'Enter to': '/code/'})


class CodeEnterView(APIView):
    """
    Authentication or registration and authorization after entered code.
    """

    def post(self, request, **kwargs):
        serializer = CodeEnterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.session.get('code') == serializer.data.get('code'):
            phone = request.session.get('phone')
            password = serializer.data.get('code')
            data = {
                'phone': phone,
                'password': password
                }
            token = TokenObtainPairSerializer(data=data)
            token.is_valid(raise_exception=True)
            request.session.pop('code', '')
            request.session.pop('phone', '')

            return Response(token.validated_data)
        else:
            return Response('Wrong code')


class CustomUserProfileView(APIView):
    """
    Profile CustomUser
    """

    def get(self, request, *args, **kwargs):
        serializer = CustomUserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = CustomUserInviteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = check_write_invite(user=request.user, invite=serializer.data.get('invite'))
        return Response(check)

