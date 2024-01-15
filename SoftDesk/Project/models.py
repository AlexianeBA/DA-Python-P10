from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    TYPE_PROJECT = (('BE', 'Back-end'),('FE', 'Front-end'),('IOS', 'IOS'), ('ANDROID', 'Android'))
    title = models.CharField(max_length=128, blank=True, verbose_name="Titre du projet")
    description = models.CharField(max_length=1020, blank=True)
    type_project = models.CharField(max_length=10, choices=TYPE_PROJECT)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='project_created_by')
    
    def __str__(self):
        return self.title