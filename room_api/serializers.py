import uuid

from rest_framework import serializers
from .models import Room, ContactUs


class RoomSerializer(serializers.ModelSerializer):
    map_location = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('id', 'room_type', 'description', 'location', 'price', 'image', 'map_location', 'latitude',
                  'longitude', 'is_water_supply', 'is_electriciy_charge', 'is_drainage_available', 'is_drinking_water')

    def get_map_location(self, instance):
        return {'latitude': instance.latitude, 'longitude': instance.longitude}


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'name', 'email', 'phone', 'message')
