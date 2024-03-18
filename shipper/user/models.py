from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    is_seller = models.BooleanField(null=False)
    phone_number = models.IntegerField(null=False)
    orders = models.TextField(null=True)
    address = models.TextField(null=True)
    # profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.username