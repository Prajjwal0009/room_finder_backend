from rest_framework import routers
from .viewsets import RoomViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
