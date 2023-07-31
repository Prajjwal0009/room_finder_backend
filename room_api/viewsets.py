from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer
from .filters import RoomFilter


# Create your views here
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter

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


