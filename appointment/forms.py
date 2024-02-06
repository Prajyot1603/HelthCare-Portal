from django import forms
from .models import Appointment
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'Doctor_Name': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
            'date_of_schedule': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_of_schedule': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Entered_by': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
        }


        

    
