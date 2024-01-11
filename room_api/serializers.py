import uuid

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import BookedRoom, Room, ContactUs,AssignedBookedRoom

User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_type', 'description', 'location', 'price', 'image', 'longitude', 'latitude',
                  'is_water_supply', 'is_electriciy_charge', 'is_drainage_available', 'is_drinking_water',
                  'booked_by')
        
    def create(self, validated_data):
        # Extract the 'image' data from the validated data
        image_data = validated_data.pop('image', None)
        instance = super(RoomSerializer, self).create(validated_data)  # Call the super create method
        if image_data:
            instance.image = image_data  # Assign the image to the 'image' field of the instance
            instance.save()
        return instance
    
class BookingSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = BookedRoom
        fields = ('id', 'room', 'name', 'email', 'phone', 'desc','booking_date')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['room'] = instance.room_id  # Display only the room ID
        return representation

class AssignedBookedRoomSerializer(serializers.ModelSerializer):
    room_id = serializers.UUIDField(write_only=True)
    booking_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = AssignedBookedRoom
        fields = ('id', 'room_id', 'booking_id', 'assign_date')

class RoomListSerializer(serializers.ModelSerializer):
    map_location = serializers.SerializerMethodField()
    bookings = BookingSerializer(many=True, read_only=True)
    assigned_room_data = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('id', 'room_type', 'description', 'location', 'price', 'image', 'map_location',
                  'is_water_supply', 'is_electriciy_charge', 'is_drainage_available', 'is_drinking_water',
                  'get_content_type_id', 'is_booked', 'bookings', 'is_assigned', 'assigned_room_data','booked_by')

    def get_map_location(self, instance):
        return {'latitude': instance.latitude, 'longitude': instance.longitude}

    def get_bookings(self, instance):
        if instance.is_booked:
            bookings = BookedRoom.objects.filter(room=instance)
            serializer = BookingSerializer(bookings, many=True)
            return serializer.data
        return None

    def get_assigned_room_data(self, instance):
        if instance.is_assigned:
            assigned_books = AssignedBookedRoom.objects.filter(room=instance)
            if assigned_books.exists():
                # Assuming you want details of the first assigned booked room
                assigned_room = assigned_books.first()
                serializer = AssignedBookedRoomSerializer(assigned_room)
                return serializer.data
        return None

    def create(self, validated_data):
        image_data = validated_data.pop('image_data', None)
        instance = super(RoomListSerializer, self).create(validated_data)  # Update the super call
        if image_data:
            instance.image_data = image_data
            instance.save()
        return instance
    
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




class UserStaffUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        fields = ('email',)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
