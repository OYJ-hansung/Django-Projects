from django.contrib import admin
from passengerInfoApp.models import Passenger


class PassengerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'rewardPoints']

admin.site.register(Passenger, PassengerAdmin)
