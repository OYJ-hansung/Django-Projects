from django import forms
from movieInfoApp.models import Movie

class movieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'



