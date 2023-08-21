from random import choice, randint
from django.shortcuts import get_object_or_404

from users.models import CustomUser


def generate_code():
    """ Generate authentication code."""
    return randint(1000, 9999)


def generate_invite():
    """ Generate invite. """
    invite = ''
    for x in range(6):
        invite = invite + choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    return invite


def check_write_invite(user, invite):
    """ Checking and writing parent invite."""
    if user.parent is None and user.invite != invite:
        user_parent = get_object_or_404(CustomUser, invite=invite)
        user.parent = user_parent
        user.save()
        return 'Invite write'
    else:
        return 'Too many invite'


