from django.shortcuts import render, get_object_or_404
from .models import Testimonial
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from rooms.models import Room
from .forms import TestimonialForm

# Create your views here.
def testimonial_view(request):
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST)
        
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.user = request.user  
            testimonial.save()
            messages.success(request, 'Your testimonial has been submitted!')
            return redirect('testimonial_view')  
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    
    else:
        testimonial_form = TestimonialForm()

    context = {
        'testimonial_form': testimonial_form,
    }
    
    return render(request, 'testimonials/testimonials.html', context)