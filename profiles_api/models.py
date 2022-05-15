from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
class userProfileManager(BaseUserManager):
    """Manager para perfil de usuario"""

    def create_user(self, email, name, password=None):
        """Nuevo usuario"""
        if not email:
            raise ValueError('Usuario debe de tener un email')

        email = self.normalize_email(email)
        user = self.model (email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



# Create your models here.


class userProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = userProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name (self):
        #Obtener nombre completo
        return self.name

    def get_short_name (self):
        #Obtener nombre corto
        return self.name

    def __str__(self):
        ''' Retornar cadena representando nuestro usuario'''
        return self.email

class ProfileFeedItem(models.Model):
    """Perfil status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retornar el nombre como cadena"""
        return self.status_text
