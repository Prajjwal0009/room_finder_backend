from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import AssignedBookedRoom, Room, ContactUs, BookedRoom
from .serializers import RoomSerializer, ContactUsSerializer, RoomListSerializer, BookingSerializer, \
    UserStaffUpdateSerializer, UserListSerializer,AssignedBookedRoomSerializer
from .filters import RoomFilter

# Create your views here
User = get_user_model()


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAuthenticated]
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


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookedRoom.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')  # Get the room data from the request data

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({'error': 'Room does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(room=room)  # Save the booking with the room association

            # Update the room's is_booked status
            room.is_booked = True
            room.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignedBookedRoomViewSet(viewsets.ViewSet):
    serializer_class = AssignedBookedRoomSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            room_id = serializer.validated_data['room_id']
            booking_id = serializer.validated_data['booking_id']

            try:
                room = Room.objects.get(id=room_id)
                booked_room = BookedRoom.objects.get(id=booking_id)

                assigned_booking = AssignedBookedRoom.objects.create(room=room, booked_room=booked_room)

                # Update is_assigned field of the Room instance
                room.is_assigned = True
                room.save()

                return Response({'message': 'Assigned room successfully.', 'data': AssignedBookedRoomSerializer(assigned_booking).data})
            except (Room.DoesNotExist, BookedRoom.DoesNotExist) as e:
                return Response({'error': 'Invalid Room ID or Booking ID'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class UserStaffUpdateViewSet(viewsets.ViewSet):
    # permission_classes = [IsAdminUser]

     def list(self, request):
        queryset = User.objects.filter(is_staff=True, is_superuser=False)
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

     def create(self, request, *args, **kwargs):
            serializer = UserStaffUpdateSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data['email']

                try:
                    user = User.objects.get(email=email)
                    user.is_staff = True
                    user.save()
                    return Response({'detail': f'is_staff status updated for user with email {email}'},
                                    status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    return Response({'detail': f'User with email {email} does not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

