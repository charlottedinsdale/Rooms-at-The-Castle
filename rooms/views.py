from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Room, RoomAvailability
from testimonials.models import Testimonial

# Create your views here.
class HomePage(generic.ListView):
    """
    Displays home page"
    """
    queryset = Testimonial.objects.all()
    template_name = 'home.html'

class ContactPage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'contact.html'

class RoomsPage(generic.ListView):
    queryset = Room.objects.all()
    template_name = 'rooms/rooms.html'

def room_detail(request, slug): 
    queryset = Room.objects.all()
    room = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "rooms/room_detail.html",
        {
            "room": room,
        }
    )
