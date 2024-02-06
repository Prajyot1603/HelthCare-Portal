from django import forms
from .models import Products
from django.contrib.auth.models import User


class ProductRegistration(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Product_name','company_name','Product_image','Product_price','EnteredBy']

    
    Product_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'})
    )

    company_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'company_name'})
    )

    Product_image = forms.ImageField(
        widget = forms.FileInput(attrs={'class':'form-control'})
    )

    Product_price = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'price','min':'1'})
    )
    
    EnteredBy = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'})
    )
    

    