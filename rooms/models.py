from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    number_of_beds = models.IntegerField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return f"{self.name} | {self.number_of_beds} bed"

class RoomAvailability(models.Model):
    AVAILABLE = 'Available'
    UNAVAILABLE = 'Unavailable'

    AVAILABILITY_STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="availability")
    start_date = models.DateField()
    end_date = models.DateField()
    availability_status = models.CharField(max_length=12, choices=AVAILABILITY_STATUS_CHOICES, default=AVAILABLE)
