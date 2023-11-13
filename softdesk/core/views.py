from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Contributor, Issue, Project
from .permissions import (IsAuthor, IsProjectContributor,
                          IsProjectContributorRelatedIssue)
from .serializers import (CommentSerializer, ContributorSerializer,
                          IssueSerializer, ProjectSerializer)


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthor]

    def perform_create(self, serializer):
        new_project = serializer.save(author=self.request.user)
        Contributor.objects.create(project=new_project, user=self.request.user)


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated, IsProjectContributorRelatedIssue]

    def get_queryset(self):
        project_id = self.kwargs["id_project"]
        return Issue.objects.filter(project=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs["id_project"]
        serializer.save(author=self.request.user, project_id=project_id)

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

        if is_assigned_user_contributor and is_authenticated_user_contributor:
            serializer.save()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]
