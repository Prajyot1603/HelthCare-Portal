from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from doctor.models import Doctors
from .models import Appointment
from .forms import AppointmentForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login') 
def schedule_appointment(request):
    doctors = Doctors.objects.all()
    user = User.objects.all()

    if request.method == 'POST':
        doctor_id = request.POST.get('Doctor_Name')
        date = request.POST.get('Date_of_Schedule')
        time = request.POST.get('Time_of_Schedule')
        Entered_by = request.POST.get('Entered_by')

        doctor = Doctors.objects.get(id=doctor_id)
        enteredby = User.objects.get(id=Entered_by)
        appointment = Appointment(
            Doctor_Name=doctor,
            Date_of_Schedule = date,
            Time_of_Schedule = time,
            Entered_by = enteredby
        )

        appointment.save()
    
        messages.success(request,'Appointment Added Successfully')

    
    context={
        'doctors':doctors,
        'user':user
    }
    return render(request,'appointment/schedule_appointment.html',context)

def update_appointment(request, pk):
    obj = Appointment.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        messages.success(request,'Appointment Updated Successfully')
                
    else:
    
        form = AppointmentForm(instance=obj)
    
    context = {'form': form}
    return render(request, 'appointment/updateappointment.html', context)

def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'appointment/list.html', context)


def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        appointment.delete()
        messages.success(request,'Appointment Cancel Successfully')

        return redirect('appointment_list')
    
    context = {'appointment': appointment}

    return render(request, 'appointment/delete_app.html', context)

def todays_schedule(request):
    today = datetime.now().date()
    result = Appointment.objects.filter(Date_of_Schedule=today)
    context={
            'object':result
        }
    return render(request,'appointment/search.html',context)
