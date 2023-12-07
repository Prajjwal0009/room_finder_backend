import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    price__range = django_filters.RangeFilter(field_name='price')
    is_booked = django_filters.BooleanFilter(field_name='is_booked')
    is_assigned = django_filters.BooleanFilter(field_name='is_assigned')


    class Meta:
        model = Room
        fields = {
            'room_type': ['in'],
            'location': ['exact', 'icontains'],
            'price': ['exact']
        }
