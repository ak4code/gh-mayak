from rest_framework import routers
from hotel.views import BookingViewSet

router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)
