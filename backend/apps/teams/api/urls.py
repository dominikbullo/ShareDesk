from rest_framework.routers import DefaultRouter

from apps.teams.api.views import TeamViewSet

app_name = 'teams'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="teams")

urlpatterns = []
