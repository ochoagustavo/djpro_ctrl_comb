from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(_("Nombre de usuario"),max_length=150)
    first_name = models.CharField(_("Nombre"),max_length=150)
    last_name = models.CharField(_("Apellido"),max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = ["username","first_name"]  
    
    def __str__(self):
        return self.email
    