from django.contrib import admin
from .models import Room, Booking, Review, AddModel

# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(AddModel)