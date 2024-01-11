from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from room_api.routers import router as room_finder
from rest_framework import routers

from room_api.views import registration_view, login_view, logout_view

router = routers.DefaultRouter()
router.registry.extend(room_finder.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

# Configuring media URL for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
