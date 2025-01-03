import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rooms.models import Room, RoomAvailability

# Create your models here.
class Booking(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booking")
    guests = models.PositiveIntegerField()
    def clean(self):
        """Custom validation to check that the number of guests is within room capacity."""
        if self.guests < 1:
            raise ValidationError('Guests must be at least 1.')
        if self.guests > self.room.capacity:
            raise ValidationError(f'Cannot book more than {self.room.capacity} guests for this room.')
    def __str__(self):
        return f"Booking Reference: {self.reference} made by {self.user}"

class BlockRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="blocking")
    start_date = models.DateField
    end_date = models.DateField