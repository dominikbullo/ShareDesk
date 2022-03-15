from rest_framework.routers import DefaultRouter

from apps.teams.api.views import TeamViewSet
from apps.workspaces.api.views import WorkspaceViewSet

app_name = 'workspaces'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"workspaces?", WorkspaceViewSet, basename="workspaces")

urlpatterns = []
