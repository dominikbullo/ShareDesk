from django.conf.urls import include
from django.urls import path

from core import router as custom_router

from apps.users.api.urls import router as users_router
from apps.teams.api.urls import router as teams_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Settings
router = custom_router.DefaultRouter()
router.trailing_slash = '/?'
router.extend(users_router)
router.extend(teams_router)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("", include(router.urls)),
    path("", include("apps.users.api.urls")),
    path("", include("apps.teams.api.urls")),
]
