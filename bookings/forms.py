from django import forms
from .models import Booking
from rooms.models import RoomAvailability

class BookingForm(forms.ModelForm):
    guests = forms.IntegerField(min_value=1, label="Number of Guests")
    start_date = forms.DateField(widget=forms.HiddenInput())  # Dates will be selected through the calendar
    end_date = forms.DateField(widget=forms.HiddenInput())    

    class Meta:
        model = Booking
        fields = ['guests', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        room = kwargs.pop('room', None)  
        super(BookingForm, self).__init__(*args, **kwargs)

        if room:
            # Set the max value for guests based on room capacity
            self.fields['guests'].widget = forms.NumberInput(attrs={
                'min': 1,
                'max': room.capacity,
                'value': 1  # Default value
            })

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            # Ensure start date is before the end date
            if start_date > end_date:
                raise forms.ValidationError("End date must be after start date.")

        return cleaned_data