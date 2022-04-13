from django import forms
from django.core import validators

class UserLogin(forms.Form):
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user_cleaned_data = super().clean()
        inputpassword = user_cleaned_data['password']
        if len(inputpassword) <8:
            raise forms.ValidationError('The password should be at least 8 characters')
        for letter in inputpassword:
            if letter.isupper():
                return
        else:
            raise forms.ValidationError('The password should include at least one capital letter')