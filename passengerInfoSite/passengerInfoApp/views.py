from django.shortcuts import render
from passengerInfoApp.models import Passenger

# Create your views here.
def passengerdata(request):
    passengers = Passenger.objects.all()
    passengerDict = {
        'passengers': passengers
    }
    return render(request, 'passengerInfoApp/passengerInfo.html', passengerDict)
