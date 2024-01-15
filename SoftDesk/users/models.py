from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser, Group
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    # STATUT = (('option1', 'Chef de projet')('option2', 'Manager'),('option3', 'Employé'))
    CHOICES = (('option1', 'Oui'), ('option2', 'Non'))
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128, blank=False)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    can_be_contacted = models.CharField(max_length=7, choices = CHOICES, default='Oui')
    can_data_be_shared = models.CharField(max_length=7, choices = CHOICES, default='Oui')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username
    
    @property
    def age(self):
        if self.date_of_birth:
            today = datetime.now().date()
            dob = self.date_of_birth
            return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return None

    def save(self, *args, **kwargs):
        if self.age is not None and self.age < 15:
            raise ValueError("L'utilisateur doit avoir au moins 15 ans pour créer un espace.")
        super().save(*args, **kwargs)
class Project(models.Model):
    TYPE_PROJECT = (('option1', 'Option 1'),('option2', 'Option 2'),('option3', 'Option 3'))
    name = models.CharField(max_length=128, blank=True, verbose_name="Nom du projet")
    description = models.CharField(max_length=1020, blank=True)
    type_project = models.CharField(max_length=10, choices=TYPE_PROJECT)
    created_at = models.DateField(auto_now_add=True)