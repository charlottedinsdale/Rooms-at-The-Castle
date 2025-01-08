from django.db import models
from datetime import datetime
from rooms.models import Room
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="testimonial")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="testimonial", blank=True)
    content = models.TextField(max_length=5000)
    image = CloudinaryField('image', blank=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} wrote a testimonial!"

