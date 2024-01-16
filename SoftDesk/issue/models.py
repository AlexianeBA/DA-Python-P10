from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=128, blank=False)
    