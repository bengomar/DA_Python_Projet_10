from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Contributor, Issue, Project
from .permissions import IsAuthor, IsContributor, IsIssueContributor
from .serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsContributor]

    def perform_create(self, serializer):
        new_project = serializer.save(author=self.request.user)
        Contributor.objects.create(project=new_project, user=self.request.user)


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated, IsIssueContributor, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        # Contributor.objects.create(project=new_issue.project, user=self.request.user)

    def perform_update(self, serializer):
        current_issue = serializer.instance
        project = current_issue.project
        assign_to = serializer.validated_data.get("assign_to")
        is_assigned_user_contributor = Contributor.objects.filter(
            project=project, id=assign_to.id
        ).exists()
        is_authenticated_user_contributor = Contributor.objects.filter(
            project=project, user=self.request.user
        ).exists()
        print(project, assign_to)
        print(
            "----------------->",
            is_authenticated_user_contributor,
            is_assigned_user_contributor,
        )

        if is_assigned_user_contributor and is_authenticated_user_contributor:
            serializer.save()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        # Pass the authenticated user to the serializer during creation
        serializer.save(author=self.request.user)


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]
