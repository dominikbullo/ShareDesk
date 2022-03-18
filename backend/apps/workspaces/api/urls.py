from rest_framework.routers import DefaultRouter

from apps.workspaces.api.views import WorkspaceViewSet, SpotIssueViewSet, SpotViewSet

app_name = 'workspaces'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"spots?", SpotViewSet, basename="spots")
router.register(r"spots?-issues?", SpotIssueViewSet, basename="spot_issues")

router.register(r"workspaces?", WorkspaceViewSet, basename="workspaces")

urlpatterns = []
