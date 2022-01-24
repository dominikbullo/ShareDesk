from rest_framework.routers import DefaultRouter

from apps.reservations.api.views import ReservationViewSet

app_name = 'reservations'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register(r"reservations", ReservationViewSet, basename="reservations")

urlpatterns = []
