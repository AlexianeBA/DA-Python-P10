from django.conf import settings
from django.db import models
from Project.models import Project


class Issue(models.Model):
    TAG_CHOICES = [
        ('BUG', 'Bug'), ('FEATURE', 'Amélioration'), ('TASK', 'Tâche')
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Faible'), ('MEDIUM', 'Moyenne'), ('HIGH','Haute')
    ]
    STATUS_CHOICES = [
        ('TODO', 'A faire'), ('INPROGRESS','En cours'), ('FINISHED', 'Fini')
    ]

    title = models.CharField(max_length=128, blank=False)
    description = models.TextField(max_length=1028, blank=False)
    tag = models.CharField(max_length=7, choices=TAG_CHOICES)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TODO')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issue_related')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_created_by')
    assigned = models.ForeignKey('users.User', on_delete=models.RESTRICT, related_name='issue_assigned_to')  # Utilisez la chaîne de caractères pour l'importation tardive
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title