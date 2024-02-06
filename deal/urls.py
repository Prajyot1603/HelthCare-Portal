from django.urls import path
from . import views


urlpatterns = [
    path('deal/',views.deal_details,name='deal'),
    path('deal_list/', views.deal_list, name='deal_list'),
    path('delete/<int:pk>', views.delete_deal, name='delete_deal'),
    path('update/<int:pk>/', views.update_deal, name='update_deal'),

]