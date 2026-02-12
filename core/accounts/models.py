from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(max_length=255, unique=True)
   is_staff = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   # is_verified = models.BooleanField(default=False)

   created_date = models.DateTimeField(auto_now_add=True)
   updated_date = models.DateTimeField(auto_now=True)

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []

   def __str__(self):
      return self.email



    