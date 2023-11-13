from rest_framework.serializers import ModelSerializer

from .models import Comment, Contributor, Issue, Project


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "author",
            "assign_to",
            "status",
            "priority",
            "tag",
            "project",
            "date_created",
        ]
        read_only_fields = ["id", "author", "date_created"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "issue", "description", "date_created"]
        read_only_fields = ["id", "author", "date_created"]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "date_created"]
        read_only_fields = ["id", "date_created"]


class ProjectSerializer(ModelSerializer):
    # issues = IssueSerializer(many=True)
    class Meta:
        model = Project
        # fields = ["id", "title", "author", "description", "type", "date_created", "issues"]
        fields = ["id", "title", "author", "description", "type", "date_created"]
        read_only_fields = ["id", "author", "date_created"]
