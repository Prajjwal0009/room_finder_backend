import uuid

from django.db import models
from model_utils import Choices

from model_utils.fields import StatusField


# Create your models here.
class Room(models.Model):
    status_choices = Choices('flat', '1Room', '2Room')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type = StatusField(choices_name="status_choices")
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, default='default_image.jpg')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_water_supply = models.BooleanField(null=True, blank=True, default=True)
    is_electriciy_charge = models.BooleanField(null=True, blank=True, default=True)
    is_drainage_available = models.BooleanField(null=True, blank=True, default=True)
    is_drinking_water = models.BooleanField(null=True, blank=True, default=True)


class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
