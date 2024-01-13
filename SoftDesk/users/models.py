from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128, blank=False)
    age = models.IntegerField(blank=True, null=True)
    
    # Add related_name to resolve clash
    groups = models.ManyToManyField(Group, related_name='user_set_custom')
    user_permissions = models.ManyToManyField(Permission, related_name='user_set_custom')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username