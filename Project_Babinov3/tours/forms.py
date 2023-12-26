from django import forms
from .models import Countries, Tours

class ToursForm(forms.ModelForm):
    class Meta:
        model = Tours
        fields = ['title', 'countries', 'hotel', 'chel', 'price', 'list']

class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = ['name']