from . import views
from django.urls import path

urlpatterns = [
    path('testimonials/', views.TestimonialsPage.as_view(), name='testimonials'),
]