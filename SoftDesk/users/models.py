
from django.db import models

from django.contrib.auth.models import AbstractUser
from datetime import datetime
from Project.models import Project

# Create your models here.
class User(AbstractUser):
    # STATUT = (('option1', 'Chef de projet')('option2', 'Manager'),('option3', 'Employé'))
    CHOICES = (('option1', 'Oui'), ('option2', 'Non'))
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128, blank=False)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    can_be_contacted = models.CharField(max_length=7, choices = CHOICES, default='Oui', verbose_name="Peut être contacté?")
    can_data_be_shared = models.CharField(max_length=7, choices = CHOICES, default='Oui', verbose_name='Peut-on partager les données?')
    is_active = models.BooleanField(default=True)
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
        self.set_password(self.password)
        super().save(*args, **kwargs)


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_contributor')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_contributor')
    # issue = 
    # comment =
    
    
    def __str__(self):
        return f'{self.user}'