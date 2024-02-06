from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from appointment.views import appointment_list
from product.views import add
from dashboard.views import dashboard_view
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,'base/register.html',{'form_data':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,'Account created Successfully for ' + user_name)
            return redirect(register)
        
        else:
            return render(request,'base/register.html',{'form_data':form})
       
    return render(request,'base/register.html',{'form_data':form})


class MyLoginView(LoginView):
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,'Invalid Username or Password')
        return redirect('/')


class MyLogoutView(LogoutView):   
    def form_valid(self):
        messages.error(self.request,"Logged Out Successfully")
        return super().form_valid(form) 

