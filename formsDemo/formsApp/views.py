from django.shortcuts import render
from . import forms

def useRegistrationView(request):
    form = forms.UserRegistrationForm
    return render(request, 'formsDemo/userRegistration.html', {'form': form})