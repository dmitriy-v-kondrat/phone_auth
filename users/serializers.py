from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from users.models import CustomUser


class PhoneEnterSerializer(serializers.ModelSerializer):
    """ Phone serializer. """
    phone = PhoneNumberField()

    class Meta:
        model = CustomUser
        fields = ('phone',)


class CodeEnterSerializer(serializers.Serializer):
    """ Code serializer. """
    code = serializers.CharField()

    class Meta:
        fields = ('code',)


class CustomUserChildrenSerializer(serializers.ModelSerializer):
    """ Serializer phone children instance."""
    class Meta:
        model = CustomUser
        fields = ('phone', )


class CustomUserProfileSerializer(serializers.ModelSerializer):
    """ Serializer profile. """
    parent_invite = serializers.CharField(source='parent.invite', default='')
    children_phone = CustomUserChildrenSerializer(source='children', many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'parent_invite', 'children_phone',
                  'last_login', 'phone', 'invite'
                  )


class CustomUserInviteSerializer(serializers.ModelSerializer):
    """ Serializer enter invite in profile user."""
    invite = serializers.CharField(max_length=6, min_length=6)
    class Meta:
        model = CustomUser
        fields = ('invite',)
