import uuid

from authentication.models import User
from django.db import models
from django.db.models import UUIDField


class Project(models.Model):
    TYPE_CHOICES = (
        ("BACK-END", "back-end"),
        ("FRONT-END", "front-end"),
        ("IOS", "IOS"),
        ("ANDROID", "Android"),
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="project_author"
    )
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default="FRONT-END")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="contributor_project"
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Issue(models.Model):
    STATUS_CHOICES = (
        ("TO_DO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("FINISHED", "Finished"),
    )
    PRIORITY_CHOICES = (("LOW", "LOW"), ("MEDIUM", "MEDIUM"), ("HIGH", "HIGH"))
    TAG_CHOICES = (("BUG", "BUG"), ("FEATURE", "FEATURE"), ("TASK", "TASK"))

    title = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default="TO_DO")
    priority = models.CharField(max_length=25, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=25, choices=TAG_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="issue_author"
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,  # On ne permet pas la suppression d'un projet ici !
        related_name="issues",
    )
    assign_to = models.ForeignKey(
        Contributor, on_delete=models.SET_NULL , null=True, related_name='issue_assigned'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="comment_author"
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description
