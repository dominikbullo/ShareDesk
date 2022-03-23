from rest_framework.routers import DefaultRouter

from apps.workspaces.api.views import WorkspaceViewSet, SpotIssueViewSet, SpotViewSet, RoomViewSet, FloorViewSet, \
    RoomLayoutViewSet

app_name = 'workspaces'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"spots?", SpotViewSet, basename="spots")
router.register(r"spots?-issues?", SpotIssueViewSet, basename="spot-issues")

router.register(r"rooms?-layouts?", RoomLayoutViewSet, basename="room-layouts")

router.register(r"workspaces?", WorkspaceViewSet, basename="workspaces")
router.register(r"floors?", FloorViewSet, basename="floors")
router.register(r"rooms?", RoomViewSet, basename="rooms")

urlpatterns = []
