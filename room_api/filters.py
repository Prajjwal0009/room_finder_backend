import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    price__range = django_filters.RangeFilter(field_name='price')

    class Meta:
        model = Room
        fields = {
            'room_type': ['in'],
            'location': ['exact', 'icontains'],
            'price': ['exact']
        }
