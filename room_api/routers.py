from rest_framework import routers
from .viewsets import RoomViewSet, ContactUsViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'contact', ContactUsViewSet)

