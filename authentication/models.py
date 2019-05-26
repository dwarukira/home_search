from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_realtor = models.BooleanField(default=False)
    avator = models.ImageField(upload_to="_users")
