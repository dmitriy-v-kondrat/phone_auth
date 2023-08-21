from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, **extra_fields):
        """
        Create and save a User with the given phone.
        """
        if not phone:
            raise ValueError('The phone must be set')
        phone = self.normalize_phone(phone)
        user = self.model(phone=phone)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    phone = PhoneNumberField(unique=True)
    invite = models.CharField(max_length=6)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING,
                               null=True, blank=True, related_name='children'
                               )

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)
