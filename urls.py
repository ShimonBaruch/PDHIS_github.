
from doctor import views

from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
   
    path('', views.doctor, name='doctor'), 
    path('login_doctor', auth_views.LoginView.as_view(template_name='login_doctor.html'),name='login_doctor'),
    path('logout_doctor', auth_views.LogoutView.as_view(template_name='logout_doctor.html'), name='logout_doctor'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('hpage', views.hpage, name='hpage'),
    path('contact', views.contact3, name='contact3'),
    path('articals', views.articals, name='articals'),
    path('calendar', views.calendar, name='calendar'),
    path('events',views.events, name='events'),
    path('checkmyfreetime/', views.checkmyfreetime, name='checkmyfreetime'),
    path('messege/',views.messege, name='messege'),
    path('contactdo',views.contactdo, name='contactdo'),
    path('doctor homepage', views.todolist, name='todolist'),
    
    
    path('login_secretary', auth_views.LoginView.as_view(template_name='login_secretary.html'), name='login_secretary'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    
    
]