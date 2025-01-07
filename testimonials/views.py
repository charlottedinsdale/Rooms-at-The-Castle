from django.shortcuts import render, get_object_or_404
from .models import Testimonial
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from rooms.models import Room, RoomAvailability

# Create your views here.
class TestimonialsPage(generic.ListView):
    queryset = (Testimonial.objects.all())
    template_name = 'testimonials/testimonials.html'