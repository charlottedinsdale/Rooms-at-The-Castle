from django.contrib import admin
from .models import Room, RoomAvailability

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomAvailability)