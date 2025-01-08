from . import views
from django.urls import path

urlpatterns = [
    path('', views.TestimonialsPage.as_view(), name='testimonials'),
]