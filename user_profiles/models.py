import os
import uuid

from django.contrib.auth.models import User
from django.db import models


def unique_avatar_name(instance, filename):
    name = uuid.uuid4()
    extension = filename.split('.')[-1]
    fullname = f'{name}.{extension}'
    return os.path.join('avatars/', fullname)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=unique_avatar_name, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
