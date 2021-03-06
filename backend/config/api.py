from django.conf.urls import include
from django.contrib.auth import logout
from django.urls import path

from apps.users.api.views import LogoutView
from core import router as custom_router

from apps.users.api.urls import router as users_router
from apps.teams.api.urls import router as teams_router
from apps.workspaces.api.urls import router as workspaces_router
from apps.reservations.api.urls import router as reservations_router

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
router.extend(workspaces_router)
router.extend(reservations_router)

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='auth_logout'),

    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("token/verify/", TokenVerifyView.as_view(), name='token_verify'),

    path("", include(router.urls)),
    path("", include("apps.users.api.urls")),
    path("", include("apps.teams.api.urls")),
    path("", include("apps.workspaces.api.urls")),
    path("", include("apps.reservations.api.urls")),
]
