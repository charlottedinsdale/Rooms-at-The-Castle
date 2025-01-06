from . import views
from django.urls import path

urlpatterns = [
    path('rooms/', views.RoomsPage.as_view(), name='rooms'),
    path('', views.HomePage.as_view(), name='home'),
]
    