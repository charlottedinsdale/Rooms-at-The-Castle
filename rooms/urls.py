from . import views
from django.urls import path

urlpatterns = [
    path('rooms/', views.RoomsPage.as_view(), name='rooms'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('', views.HomePage.as_view(), name='home'),
    path('<slug:slug>/', views.room_detail, name='room_detail'),
]
    