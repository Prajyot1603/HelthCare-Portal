from django.shortcuts import render
from doctor.models import Doctors
from product.models import Products
from appointment.models import Appointment
from deal.models import Deal
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login') 
def dashboard_view(request):
    pd = Products.objects.all().count()
    dd = Doctors.objects.all().count()
    ad = Appointment.objects.all().count()
    dld = Deal.objects.all().count()
    

    data = {'dd':dd,'pd':pd,'ad':ad,'dld':dld}
    return render(request, 'dashboard/dashboard.html',data)
    # return render(request, 'account/login.html', context)



