import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rooms.models import Room, RoomAvailability
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booking")
    guests = models.PositiveIntegerField()
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    def clean(self):
        """Custom validation to check that the number of guests is within room capacity."""
        if self.guests < 1:
            raise ValidationError('Guests must be at least 1.')
        if self.guests > self.room.capacity:
            raise ValidationError(f'Cannot book more than {self.room.capacity} guests for this room.')

    def total_price(self):
        if not self.start_date or not self.end_date:
            return 0
        num_nights = (self.end_date - self.start_date).days
        if num_nights < 1:
            return 0
        return num_nights * self.room.price_per_night

    def __str__(self):
        return f"Total Price: {booking.total_price()}. Booking Reference: {self.reference} made by {self.user}"