from django.db import models
from model_utils import Choices

from model_utils.fields import StatusField


# Create your models here.
class Room(models.Model):
    status_choices = Choices('flat', '1Room', '2Room')

    room_type = StatusField(choices_name="status_choices")
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, default='default_image.jpg')