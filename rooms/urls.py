from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('rooms/', views.RoomsPage.as_view(), name='rooms'),
]
    