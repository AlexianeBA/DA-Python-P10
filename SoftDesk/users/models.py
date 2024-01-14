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
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username
    
    
class Project(models.Model):
    TYPE_PROJECT = (('option1', 'Option 1'),('option2', 'Option 2'),('option3', 'Option 3'))
    name = models.CharField(max_length=128, blank=True, verbose_name="Nom du projet")
    description = models.CharField(max_length=1020, blank=True)
    type_project = models.CharField(max_length=10, choices=TYPE_PROJECT)
    created_at = models.DateField(auto_now_add=True)