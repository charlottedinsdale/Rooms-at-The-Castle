from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Room, RoomAvailability

@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(RoomAvailability)