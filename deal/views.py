from django.shortcuts import render,get_object_or_404, redirect
from doctor.models import Doctors
from product.models import Products
from .models import Deal
from .forms import DealForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login') 
def deal_details(request):
    doctors = Doctors.objects.all()
    products = Products.objects.all()
    user = User.objects.all()

    if request.method == 'POST':
        doctor_id = request.POST.get('Doctor_Name')
        product_id = request.POST.get('Product_name')
        quintity = request.POST.get('Quantity')
        entered_by = request.POST.get('Entered_by')
        date = request.POST.get('Date')

        doctor = Doctors.objects.get(id=doctor_id)
        product = Products.objects.get(id=product_id)
        entered_by = User.objects.get(id=entered_by)
        deal = Deal(
            Doctor_Name=doctor,
            Product_Name=product,
            Quantity=quintity,
            Entered_by = entered_by,
            Date = date
        )

        deal.save()
        messages.success(request,'Deal Added Successfully')

        
    context={
        'doctors':doctors,
        'products':products,
        'user':user
    }
    
    return render(request,'deal/deal.html',context)


def update_deal(request, pk):
    obj = Deal.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = DealForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        messages.success(request,'Deal Updated Successfully')

                
    else:
       
        form = DealForm(instance=obj)
    
    context = {'form': form}
    return render(request, 'deal/form.html', context)


def deal_list(request):
    deals = Deal.objects.all()
    context = {'deals': deals}
    return render(request, 'deal/list.html', context)


def delete_deal(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    
    if request.method == 'POST':
        deal.delete()
        messages.success(request,'Deal Cancel Successfully')

        return redirect('deal_list')
    
    context = {'deal': deal}
    return render(request, 'deal/deletedeal.html', context)