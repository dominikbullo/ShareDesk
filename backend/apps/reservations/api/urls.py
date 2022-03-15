from rest_framework.routers import DefaultRouter

from apps.reservations.api.views import SpotReservationViewSet, SpotViewSet

app_name = 'reservations'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"spots?/reservations?", SpotReservationViewSet, basename="spot_reservations")
router.register(r"spots?", SpotViewSet, basename="spots")

urlpatterns = []
