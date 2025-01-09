from . import views
from django.urls import path

urlpatterns = [
    path('', views.testimonial_view, name='testimonials'),
]