import uuid

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Room, ContactUs

User = get_user_model()


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
