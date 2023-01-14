from pages import views
from django.urls import path

"""

"""
urlpatterns = [
    path('',views.pages,name='home'),
    path('about_us',views.about,name='about'),
    path('patient/',views.patient,name='patient'),
    path('patient_home/',views.patient_home,name='patient_home'),
    path('medical_files/',views.medical_files,name='medical_files'),
    path('appointments/',views.appointments,name='appointments'),
    path('create_appointments/',views.create_appointments,name='create_appointments'),
    path('urgent_appeal/',views.urgent_appeal,name='urgent_appeal'),
    path('messege_to_patient/',views.messege_to_patient,name='messege_to_patient'),
    path('appointment_delete/', views.appointment_delete ,name='appointment_delete'),
    path('update_appointment/', views.update_appointment ,name='update_appointment'),
    path('view_appointments/',views.view_appointments,name='view_appointments'),
    path('appointmentviasecretary/',views.messegetoseretary,name='messegetoseretary'),
    path('messegetoseretary2/',views.messegetoseretary2,name='messegetoseretary2'),

]
