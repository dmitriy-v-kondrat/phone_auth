

from django.contrib.auth.backends import BaseBackend

from users.models import CustomUser
from users.services import generate_invite

class CustomerBackend(BaseBackend):

    def authenticate(self, request, phone=None, password=None):
        phone = phone
        if CustomUser.objects.filter(phone=phone).exists():
            user = CustomUser.objects.get(phone=phone)

        else:
            invite = generate_invite()
            user = CustomUser.objects.create(phone=phone, invite=invite)
        return user

    def get_user(self, phone):
        try:
            return CustomUser.objects.get(pk=phone)
        except CustomUser.DoesNotExist:
            return None
