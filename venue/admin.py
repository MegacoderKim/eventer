from django.contrib import admin
# Register your models here.
from .models import Venue, Photo, Facility


class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact']


admin.site.register(Venue, VenueAdmin)
admin.site.register(Photo)
admin.site.register(Facility)