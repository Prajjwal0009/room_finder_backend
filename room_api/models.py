import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from model_utils import Choices

from model_utils.fields import StatusField


# Create your models here.


class Room(models.Model):
    status_choices = Choices('flat', '1Room', '2Room')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type = StatusField(choices_name="status_choices", default='flat')
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_water_supply = models.BooleanField(null=True, blank=True, default=True)
    is_electriciy_charge = models.BooleanField(null=True, blank=True, default=True)
    is_drainage_available = models.BooleanField(null=True, blank=True, default=True)
    is_drinking_water = models.BooleanField(null=True, blank=True, default=True)
    is_booked = models.BooleanField(default=False)
    is_assigned = models.BooleanField(default=False)
    booked_by = models.CharField(max_length=255)

    def get_content_type_id(self):
        return ContentType.objects.get_for_model(type(self)).id


class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()


class BookedRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)


class AssignedBookedRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="assigned_bookings")
    booked_room = models.ForeignKey(BookedRoom, on_delete=models.CASCADE, related_name="booked_assignment")
    assign_date = models.DateTimeField(auto_now_add=True)
