from django import forms
from .models import *


class PartyForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name','dec','img']