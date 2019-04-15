from django import forms
from .models import addhouse

class HouseForm(forms.ModelForm):
    class Meta:
        model = addhouse
        fields =('location','address','phone_no','cover')


