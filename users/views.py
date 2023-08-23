from time import sleep

from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.serializers import CodeEnterSerializer, CustomUserInviteSerializer, \
    CustomUserProfileSerializer, PhoneEnterSerializer

from users.services import check_write_invite, generate_code



class PhoneEnterView(APIView):
    """
    Enter phone number. Format +11234567890.
    After follow page code/
    """

    @extend_schema(
            parameters=[PhoneEnterSerializer],
            request=PhoneEnterSerializer,
            responses={200: inline_serializer(
                    name='PhoneEnterViewResponse',
                    fields={'code': serializers.IntegerField()}
                    )
                }
            )
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

    @extend_schema(
            parameters=[CodeEnterSerializer],
            request=CodeEnterSerializer,
            responses={201: TokenObtainPairSerializer},
            )
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

            return Response(token.validated_data, 201)
        else:
            return Response('Wrong code')



class CustomUserProfileView(APIView):
    """
    Profile CustomUser
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
            parameters=[CustomUserProfileSerializer],
            request=CustomUserProfileSerializer,
            responses=CustomUserProfileSerializer,
            )
    def get(self, request, *args, **kwargs):
        serializer = CustomUserProfileSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
            parameters=[CustomUserInviteSerializer],
            request=CustomUserInviteSerializer,
            responses={201: str},
            )
    def put(self, request, *args, **kwargs):
        serializer = CustomUserInviteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = check_write_invite(user=request.user, invite=serializer.data.get('invite'))
        return Response(check)

