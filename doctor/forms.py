from django import forms
from .models import Doctors
from django.contrib.auth.models import User

class DoctorRegistration(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['Doctor_Name','Doctor_Specialisation','Doctor_Contact_Number','Doctor_Location','EnteredBy']

    
    Doctor_Name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'})
    )

    Doctor_Specialisation = forms.ChoiceField(
        choices = [
            ('Chest', 'Chest'),
            ('Heart', 'Heart'),
            ('Pathology','Pathology'),
            ('General', 'General'),
            ('Family Medicine','Family Medicine'),
            ('Orthopaedic', 'Orthopaedic'),
            ('Sergery','Sergery')
            ],
            required=True,
            widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle '})
    )

    Doctor_Contact_Number = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact_Number','min':'0','pattern':"[1-9]{1}[0-9]{9}"})
    )

    Doctor_Location = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'})
    )

    EnteredBy = forms.ModelChoiceField(queryset=User.objects.all() ,widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle '}))

