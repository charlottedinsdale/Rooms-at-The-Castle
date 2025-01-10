from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Room, RoomAvailability
from testimonials.models import Testimonial
from testimonials.forms import TestimonialForm
from django.http import HttpResponseRedirect

# Create your views here.
# class HomePage(generic.ListView):
#     """
#     Displays home page"
#     """
#     queryset = Testimonial.objects.all()
#     template_name = 'home.html'

class HomePage(generic.ListView):
    """
    Displays home page with testimonials and a form to submit a new testimonial.
    """
    model = Testimonial
    template_name = 'home.html'
    context_object_name = 'testimonials'  # Use 'testimonials' in the template

    def get_queryset(self):
        # Return only approved testimonials
        return Testimonial.objects.filter(approved=True)

    def get_context_data(self, **kwargs):
        # Add the testimonial form to the context
        context = super().get_context_data(**kwargs)
        context['testimonial_form'] = TestimonialForm()  # Add the form to the context
        return context

    def post(self, request, *args, **kwargs):
        # Handle testimonial form submission
        testimonial_form = TestimonialForm(request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Your testimonial has been submitted for approval!')
            return HttpResponseRedirect(reverse('home'))  # Redirect to home after submission
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
        
        # If the form is not valid, render the context with the form errors
        return self.get(request, *args, **kwargs)
    
def edit_testimonial(self, request, testimonial_id):
        if request.method == "POST":
            testimonial = get_object_or_404(Testimonial, pk=testimonial_id, user=request.user)
            testimonial_form = TestimonialForm(data=request.POST, instance=testimonial)

            if testimonial_form.is_valid() and testimonial.user == request.user:
                testimonial = testimonial_form.save(commit=False)
                testimonial.approved = False
                testimonial.save()
                messages.add_message(request, messages.SUCCESS, 'Testimonial updated and awaiting approval!')
            else:
                messages.add_message(request, messages.ERROR,
                                    'Error updating testimonial!')

        return HttpResponseRedirect(reverse('home'))

def delete_testimonial(self, request, testimonial_id):
        if request.method == "POST":
            testimonial = get_object_or_404(Testimonial, pk=testimonial_id, user=request.user)

            if testimonial.user == request.user:
                testimonial.delete()
                messages.add_message(request, messages.SUCCESS, 'Testimonial deleted!')
            else:
                messages.add_message(request, messages.ERROR,
                                    'Error deleting testimonial!')

        return HttpResponseRedirect(reverse('home'))

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
