from rest_framework import routers
from hotel.views import BookingViewSet, FeedbackViewSet

router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'feedback', FeedbackViewSet)
