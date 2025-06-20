from django.contrib import admin
from .models import Trip, Reservation, Expense, ItineraryItem, TodoCategory, TodoItem

# Register your models here.
admin.site.register([Trip, Reservation, Expense, ItineraryItem, TodoCategory, TodoItem])