from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctors(models.Model):
    SPECIALISATION_CHOICES = [
        ('Chest', 'Chest'),
        ('Heart', 'Heart'),
        ('Pathology','Pathology'),
        ('General', 'General'),
        ('Family Medicine','Family Medicine'),
        ('Orthopaedic', 'Orthopaedic'),
        ('Sergery','Sergery')
        # Add more choices 
    ]

    Doctor_Name = models.CharField(max_length=100)
    Doctor_Specialisation = models.CharField(max_length=100,choices=SPECIALISATION_CHOICES)
    Doctor_Contact_Number = models.CharField(max_length=10)
    Doctor_Location = models.CharField(max_length=100)
    EnteredBy = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = 'Doc'

    def __str__(self):
        return self.Doctor_Name