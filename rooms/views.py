from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Room, RoomAvailability

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

class RoomsPage(generic.ListView):
    queryset = (Room.objects)
    template_name = 'rooms/rooms.html'
