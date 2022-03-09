from rest_framework.routers import DefaultRouter

from apps.users.api.views import UserViewSet

app_name = 'users'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"users?", UserViewSet, basename="user")

urlpatterns = []
