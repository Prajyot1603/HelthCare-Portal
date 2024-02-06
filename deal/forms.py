from django import forms
from .models import Deal



class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'
        widgets = {
            'Doctor_Name': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
            'Product_Name': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
            'Quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'Entered_by': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
        }