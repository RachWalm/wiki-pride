from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time')  # Fields to display in the list view
    search_fields = ('title', 'description')  # Fields to search by in the admin interface
    list_filter = ('date',)  # Filters to use in the admin interface
    ordering = ('-date',)  # Default ordering of events

