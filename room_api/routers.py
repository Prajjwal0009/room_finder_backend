from rest_framework import routers
from .viewsets import RoomViewSet, ContactUsViewSet, BookingViewSet, UserStaffUpdateViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'contact', ContactUsViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'update-staff', UserStaffUpdateViewSet, basename='update-staff')


