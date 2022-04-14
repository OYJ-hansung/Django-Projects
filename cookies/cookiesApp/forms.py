from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=20)
    quantity = forms.IntegerField()
         