from django.shortcuts import render
from . import forms

def loginView(request):
    form = forms.UserLogin()
    if request.method == 'POST':
        form=forms.UserLogin(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("userName :", form.cleaned_data['userName'])
            print("password :", form.cleaned_data['password'])
    return render(request, 'loginApp/login.html', {'form': form})

