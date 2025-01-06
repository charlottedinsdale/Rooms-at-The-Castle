from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
from rooms.models import Room, RoomAvailability

# Create your views here.
def booking_view(request, slug):
    queryset = Room.objects.all()
    room = get_object_or_404(queryset, slug=slug)
    return render(request, 'bookings/booking.html', {'room': room})

@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        room = request.POST.get('room')
        user = request.POST.get('user')  
        guests = request.POST.get('guests')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Create the booking
        room = Room.objects.get(id=room_id)
        booking = Booking.objects.create(
            user=user,
            room=room,
            guests=guests,
            start_date=start_date,
            end_date=end_date
        )

        # Update RoomAvailability to mark these dates as unavailable
        RoomAvailability.objects.create(
            room=room,
            start_date=start_date,
            end_date=end_date,
            availability_status=RoomAvailability.UNAVAILABLE
        )

        return JsonResponse({'status': 'success', 'booking_reference': str(booking.reference)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)