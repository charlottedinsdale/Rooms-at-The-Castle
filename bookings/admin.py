from django.contrib import admin
from .models import Booking, BlockRoom
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Booking)
admin.site.register(BlockRoom)