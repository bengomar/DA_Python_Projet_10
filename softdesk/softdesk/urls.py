from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserViewset
from core.views import ProjectViewset, IssueViewset, CommentViewset, ContributorViewset


router = routers.SimpleRouter()
router.register('users', UserViewset, basename='users')
router.register('projects', ProjectViewset, basename='projects')

router.register('projects/(?P<id_project>\d+)/issues', IssueViewset, basename='issues')
router.register('projects/(?P<id_project>\d+)/issues/(?P<id_issue>\d+)/comments', CommentViewset, basename='comments')
router.register('contributors', ContributorViewset, basename='contributors')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]

# path("ticket/<int:ticket_id>/edit-ticket/", edit_ticket, name="edit_ticket")