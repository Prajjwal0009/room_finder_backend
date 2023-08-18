from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Room, ContactUs
from .serializers import RoomSerializer, ContactUsSerializer, RoomListSerializer
from .filters import RoomFilter


# Create your views here
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return []
        return super().get_permissions()
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return RoomListSerializer
        return RoomSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the filter parameters from the request
        params = self.request.query_params
        print("Received Filter Parameters:", params)

        # Filter the queryset using the applied filters
        price_range = params.get('price__range')
        if price_range:
            price_min, price_max = map(int, price_range.split(','))
            queryset = queryset.filter(price__range=(price_min, price_max))

        return queryset


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
