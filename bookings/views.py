# from django.shortcuts import render, get_object_or_404
# from django.views import generic
# from django.contrib import messages
# from django.urls import path, include
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Booking
# from rooms.models import Room, RoomAvailability

# # Create your views here.
# def booking_view(request, slug):
#     queryset = Room.objects.all()
#     room = get_object_or_404(queryset, slug=slug)
#     return render(request, 'bookings/booking.html', {'room': room})

# @csrf_exempt
# def create_booking(request):
#     if request.method == 'POST':
#         room = request.POST.get('room')
#         user = request.POST.get('user')  
#         guests = request.POST.get('guests')
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')

#         # Create the booking
#         room = Room.objects.get(id=room_id)
#         booking = Booking.objects.create(
#             user=user,
#             room=room,
#             guests=guests,
#             start_date=start_date,
#             end_date=end_date
#         )

#         # Update RoomAvailability to mark these dates as unavailable
#         RoomAvailability.objects.create(
#             room=room,
#             start_date=start_date,
#             end_date=end_date,
#             availability_status=RoomAvailability.UNAVAILABLE
#         )

#         return JsonResponse({'status': 'success', 'booking_reference': str(booking.reference)})
    
#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Booking
from rooms.models import Room, RoomAvailability
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime

@csrf_exempt
def booking_view(request, slug):
    # Fetch the room based on the slug
    queryset = Room.objects.all()
    room = get_object_or_404(queryset, slug=slug)

    if request.method == 'GET':
        # Fetch room availability for the calendar
        room_availabilities = RoomAvailability.objects.filter(room=room)
        
        # Prepare data for FullCalendar (in JSON format)
        availability_data = []
        for availability in room_availabilities:
            availability_data.append({
                'title': 'UNAVAILABLE' if availability.availability_status == RoomAvailability.UNAVAILABLE else 'AVAILABLE',
                'start': availability.start_date.strftime('%Y-%m-%d'),
                'end': availability.end_date.strftime('%Y-%m-%d'),
                'color': '#dc3545' if availability.availability_status == RoomAvailability.UNAVAILABLE else '#28a745',
                'display': 'background'  # This ensures the event shows as a background color
            })

        # Render the booking page with the calendar and availability data
        return render(request, 'bookings/booking.html', {
            'room': room,
            'availability_data': availability_data
        })

    elif request.method == 'POST':
        # Handle booking submission (AJAX call)
        room_id = request.POST.get('room')
        user_id = request.POST.get('user')
        guests = request.POST.get('guests')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        room = Room.objects.get(id=room_id)

        # Parse the start and end dates
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Create the booking
        booking = Booking.objects.create(
            user_id=user_id,  # Assuming user_id is being passed
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