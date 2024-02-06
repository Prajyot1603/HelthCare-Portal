from django.urls import path
from . import views

urlpatterns = [
    path('schedule/',views.schedule_appointment,name='schedule'),
    path('update/<int:pk>/', views.update_appointment, name='update_view'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('delete/<int:pk>', views.delete_appointment, name='delete_appointment'),
    path('search_list/',views.todays_schedule,name='search_list'),
]