from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import loader
from datetime import timedelta
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from django.conf import settings
from  django.core.mail import send_mail
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from secretary.forms import ContactForm 
from user.models import UserDoctor,UserPatient,UserSecretary,messegetos
from user.forms import doctor_messege_form

today = date.today()
yesterday = today - timedelta(days = 1)

def todolist(request):
    # all_tasks = TaskList.objects.all

    context = {
        'welcome_text':"welcome to PDHIS"
    }
    return render(request,'todolist.html', context)

def register(request):
    register_form = UserCreationForm()
    return render(request, 'login_doctor.html', {'register_form': register_form})

def about(request):
    return render(request, 'about.html', {})

def doctor(request):
    context = {
        'doctor_text':"welcome doctor"
    }
    print("askcmkcn")
    return render(request,'login_doctor.html', context)



def hpage(request):
    context = {
        'secretary_text':"welcome"
    }
    return render(request, 'hpage.html', context)


def contact3(request):
    
    return render(request, 'contact3.html', {})


def articals(requset):

    return render(requset, 'articals.html',{})



def events(request):
    
    return render(request, 'events.html',{})



def calendar(requset):

    return render(requset, 'checkdoctorfreetime.html',{})

def checkmyfreetime(request):
    doctor = request.POST['doctor_name']
    freetime = request.POST['date']
    starttime = request.POST['appt-time']
   
   # mydoctor = EventForDoctor.objects.filter(doctor_name=doctor)
    template = loader.get_template('checkfreetime.html')
    context = {
    'doctor': doctor,
    'freetime': freetime,
    'starttime':starttime,
    
    #'mydoctor':mydoctor, 
    }
    return HttpResponse(template.render(context, request)) 

def messege(request):
    # form =messege(request.POST)
    # sec = UserSecretary.objects.get(id=form.data['secretary'])
    # messege_ =messege()
    # messege_.messege = form.data['messege']
    # messege_.doctor =UserDoctor.objects.get(id=form.data['doctor'])
    # messege_.patient = UserPatient.objects.get(user_patient__username= request.user)
    # messege_.save()
    context= {'patient_home_text':"welcome",'form':doctor_messege_form()}
    return render(request,'messege.html',context)

def contactdo(request): 
    print("contactdo")
    form =doctor_messege_form(request.POST)
    # sec = UserSecretary.objects.get(id=form.data['secretary'])
    messege_ =messegetos()
    messege_.messege = form.data['messege']
    messege_.doctor =UserDoctor.objects.get(user_doctor__username=request.user)
    messege_.secretary = UserSecretary.objects.get(id=form.data['secretary'])
    messege_.save()
    return render(request,'hpage.html',{}) 






