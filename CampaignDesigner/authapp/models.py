from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    phone = PhoneField(verbose_name='Способы связи', blank=True,
                       help_text='конактный номер телефона')