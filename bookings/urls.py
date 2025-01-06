from . import views
from django.urls import path
from .views import booking_view, create_booking
from rooms.views import room_detail

urlpatterns = [
    path('<slug:slug>/book/', booking_view, name='bookings_view'),
]