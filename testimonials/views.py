# from django.shortcuts import render, get_object_or_404, reverse, redirect
# from .models import Testimonial
# from django.views import generic
# from django.contrib import messages
# from django.views.generic import TemplateView
# from django.http import HttpResponseRedirect
# from rooms.models import Room
# from .forms import TestimonialForm

# # Create your views here.
# def testimonial_view(request):
#     if request.method == 'POST':
#         testimonial_form = TestimonialForm(request.POST)
        
#         if testimonial_form.is_valid():
#             testimonial = testimonial_form.save(commit=False)
#             testimonial.user = request.user  
#             testimonial.save()
#             messages.success(request, 'Your testimonial has been submitted for approval!')
#             return redirect('home')  
#         else:
#             messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    
#     else:
#         testimonial_form = TestimonialForm()

#     context = {
#         'testimonial_form': testimonial_form,
#     }
    
#     return render(request, 'home.html', context)


# def edit_testimonial(request, testimonial_id):
#     """
#     View to edit testimonials
#     """
#     # Retrieve the testimonial and ensure the user is the owner
#     testimonial = get_object_or_404(Testimonial, pk=testimonial_id, user=request.user)

#     if request.method == "POST":
#         # Initialize form with POST data and instance of the testimonial to edit
#         testimonial_form = TestimonialForm(data=request.POST, instance=testimonial)

#         if testimonial_form.is_valid():
#             # Save the updated testimonial but do not approve it immediately
#             testimonial = testimonial_form.save(commit=False)
#             testimonial.approved = False  # Testimonial needs re-approval after editing
#             testimonial.save()

#             # Success message
#             messages.success(request, 'Your testimonial has been updated and is awaiting approval!')
#             return redirect('home') 

#         else:
#             # Error message
#             messages.error(request, 'There was an error updating your testimonial. Please correct the form.')

#     else:
#         # If not a POST request, pre-fill the form with the existing testimonial
#         testimonial_form = TestimonialForm(instance=testimonial)

#     context = {
#         'testimonial_form': testimonial_form,
#         'testimonial': testimonial,
#     }

#     return render(request, 'home.html', context)