from django.db import models
from doctor.models import Doctors
from product.models import Products
from django.contrib.auth.models import User
# Create your models here.

class Deal(models.Model):
    Doctor_Name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Products,on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    Date= models.DateField(default=None)
    Entered_by = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = 'Deal'

        


