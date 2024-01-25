from django.db import models
from issue.models import Issue
from django.conf import settings


# Create your models here.
class Comment(models.Model):
    description = models.CharField(max_length=128, blank=False)
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="issue_comment"
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.description}"
