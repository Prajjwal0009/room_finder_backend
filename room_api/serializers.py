import uuid

from rest_framework import serializers
from .models import Room, ContactUs


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_type', 'description', 'location', 'price', 'image', 'latitude', 'longitude')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'name', 'email', 'phone', 'message')
