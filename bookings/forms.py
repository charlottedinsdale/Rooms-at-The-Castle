from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    A form for creating and updating Booking instances.

    This class uses Django's ModelForm to generate a form based on the Booking model. 
    It includes the following features:

    - **Model**: The form is tied to the `Booking` model.
    - **Fields**: The form includes fields for room and number_of_guests.
    """
    class Meta:
        model = Booking 