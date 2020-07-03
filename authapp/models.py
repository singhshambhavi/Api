from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    email = models.CharField(verbose_name='email', max_length=255,unique=True)
    dob = models.DateField(auto_now=False, blank=False)
    REQUIRED_FIELDS=['username', 'first_name','last_name','dob']
    USERNAME_FIELD='email'

    def get_username(self):
        return self.email