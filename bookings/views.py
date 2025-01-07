# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import Booking
# from rooms.models import Room, RoomAvailability
# from django.utils.dateparse import parse_date
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from datetime import datetime

# @csrf_exempt
# def booking_view(request, slug):
#     # Fetch the room from slug
#     queryset = Room.objects.all()
#     room = get_object_or_404(queryset, slug=slug)

#     if request.method == 'GET':
#         # Fetch room availability for the calendar
#         room_availabilities = RoomAvailability.objects.filter(room=room)
        
#         # Prepare data in JSON format
#         availability_data = []
#         for availability in room_availabilities:
#             availability_data.append({
#                 'title': 'UNAVAILABLE' if availability.availability_status == RoomAvailability.UNAVAILABLE else 'AVAILABLE',
#                 'start': availability.start_date.strftime('%Y-%m-%d'),
#                 'end': availability.end_date.strftime('%Y-%m-%d'),
#                 'color': '#dc3545' if availability.availability_status == RoomAvailability.UNAVAILABLE else '#28a745',
#                 'display': 'background'  
#             })

#         # Render the booking page with the calendar and availability data
#         return render(request, 'bookings/booking.html', {
#             'room': room,
#             'availability_data': availability_data
#         })

#     elif request.method == 'POST':
#         # Handle booking submission (AJAX call)
#         room_id = request.POST.get('room')
#         user_id = request.POST.get('user')
#         guests = request.POST.get('guests')
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')

#         room = Room.objects.get(id=room_id)

#         # Parse start and end dates
#         start_date = datetime.strptime(start_date, '%Y-%m-%d')
#         end_date = datetime.strptime(end_date, '%Y-%m-%d')

#         # Create the booking
#         booking = Booking.objects.create(
#             user_id=user_id,  
#             room=room,
#             guests=guests,
#             start_date=start_date,
#             end_date=end_date
#         )

#         # Update RoomAvailability to make booking dates UNAVAILABLE
#         RoomAvailability.objects.create(
#             room=room,
#             start_date=start_date,
#             end_date=end_date,
#             availability_status=RoomAvailability.UNAVAILABLE
#         )

#         return JsonResponse({'status': 'success', 'booking_reference': str(booking.reference)})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from rooms.models import Room, RoomAvailability
from django.http import JsonResponse
import json

def booking_view(request, slug):
    queryset = Room.objects.all()
    room = get_object_or_404(Room, slug=slug)

    # Retrieve room availability data and format it for FullCalendar
    availabilities = RoomAvailability.objects.filter(room=room)
    availability_data = []

    for availability in availabilities:
        status = 'AVAILABLE' if availability.availability_status == RoomAvailability.AVAILABLE else 'UNAVAILABLE'
        availability_data.append({
            'title': status,
            'start': availability.start_date.isoformat(),
            'end': availability.end_date.isoformat(),
            'allDay': True
        })

    if request.method == 'POST':
        form = BookingForm(request.POST, room=room)
        if form.is_valid():
            # Save the booking
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user making the booking
            booking.room = room  # Set the room being booked
            booking.save()

            # Update RoomAvailability to mark booking dates as unavailable
            RoomAvailability.objects.create(
                room=room,
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                availability_status=RoomAvailability.UNAVAILABLE
            )

            return JsonResponse({'status': 'success', 'message': 'Booking successful!'})

    else:
        form = BookingForm(room=room)  # Initialize the form 

    context = {
        'room': room,
        'form': form,
        'availability_data': json.dumps(availability_data)  # Pass availability data for FullCalendar
    }

    return render(request, 'bookings/booking.html', context)