from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Defines custom User model in a LOCAL_APPS just to be easy making changes or extending in the future"""
    pass
