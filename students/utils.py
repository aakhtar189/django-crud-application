from __future__ import unicode_literals

import datetime
import math
from decimal import Decimal

from django.contrib.auth.models import User
from django.conf import settings


def create_username(name):
    """create the unique username of every new user by using its name"""
    name = ''.join(e for e in name if e.isalnum())
    name = name[:29]
    base_name = name
    ctr = 1

    while True:
        try:
            user = User.objects.get(username=name)
            name = base_name + (str(ctr))
            ctr += 1
        except User.DoesNotExist:
            break

    return name
