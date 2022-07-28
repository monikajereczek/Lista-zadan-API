from django import forms
from .models import Note
import datetime


class FilterForm(forms.Form):
    Start_date= forms.DateField()
    End_date= forms.DateField()
    widgets = {
            'Data_od': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'},),
            'Data_do': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'},),
        }
CHOICES =(
        (1, "After deadline"),
        (2, "Before deadline"),
        (3, "Without deadline"),
    )
class StatusFiler(forms.Form):
    Status = forms.TypedChoiceField(
        choices = CHOICES,
        coerce = str
    )