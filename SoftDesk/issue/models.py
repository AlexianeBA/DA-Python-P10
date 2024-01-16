from django.db import models
from Project.models import Project
from django.conf import settings
from users.models import User

# Create your models here.
class Issue(models.Model):
    TAG = [
        ('BUG', 'Bug'), ('FEATURE', 'Amélioration'), ('TASK', 'Tâche')
    ]
    PRIORITY= [
        ('LOW', 'Faible'), ('MEDIUM', 'Moyenne'), ('HIGH','Haute')
    ]
    STATUS= [('TODO', 'A faire'), ('INPROGRESS','En cours'), ('FINISHED', 'Fini')]
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=128)
    tag= models.CharField(max_length=7, choices=TAG)
    priority=models.CharField(max_length=6, choices=PRIORITY)
    status=models.CharField(max_length=10, choices=STATUS, default='TODO')
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issue_related')
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='issue_created_by')
    assigned=models.ForeignKey(User, on_delete=models.RESTRICT, related_name='issue_assigned_to')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title