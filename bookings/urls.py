from . import views
from django.urls import path
from .views import booking_view
from rooms.views import room_detail

urlpatterns = [
    path('<slug:slug>/book/', booking_view, name='booking_view'),
]
