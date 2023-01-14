from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse , JsonResponse
from django.template import loader
# from .models import Patient, Event, Payment
from datetime import date
from datetime import timedelta
import calendar
from calendar import HTMLCalendar
from django.conf import settings
from  django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import ContactForm 
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from user.models import UserPatient,Appointments,UserDoctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import views
from user.forms import Appointments_Form,AppointmentsForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            message = form.cleaned_data['message']

            html = render_to_string('html/contactmail.html', {'name':name, 'email':email, 'message':message})
            print('the form was valid')
            send_mail('Scheduling an Appointment', 'message', 'p1312719@gmail.com', [email], html_message=html)
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,'html/trialmail.html',{'form':form})
   


def turnoffalert(request):
    messages.add_message(request,messages.SUCCESS,'THE ALERT WAS TAKEN CARE OF')
    return render(request,'html\homemsecretary.html')


def notify(request):
    messages.add_message(request, messages.WARNING,'YOU HAVE A NEW APPOINTMENT')
    return render(request,'html/notification.html')



def upload(request):
    
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        
        form =Appointments_Form(request.POST)
        if form.is_valid() and request.POST['patient_name']:
            print(patient_name)
            print(patient_name)
            user = UserPatient.objects.get(user_patient__last_name=patient_name)
            app = Appointments.objects.get(patient=user,appointment_date=form.data['appointment_date'],start_time=form.data['start_time'])
            if request.FILES['payment_file'] != None:
               app.payment_file = request.FILES['payment_file']
            # if request.FILES['medical_file'] !=None:
            #    app.medical_file=request.FILES['medical_file']
            app.save()
            return render(request,'html/homemsecretary.html')

        
        
        else:
            context= { 'madicl_files_text':"welcome choose from the following",'Appointments_Form':Appointments_Form,'Appointment':Appointments.objects.all()}
            return render(request,'html/load.html',context)
       

 
            

    context= { 'madicl_files_text':"welcome choose from the following",'Appointments_Form':Appointments_Form,'Appointment':Appointments.objects.all()}
    return render(request,'html/load.html',context)
   


today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days=1)


def medicalsecretary_home(request):
    template = loader.get_template('html/homemsecretary.html')
    return HttpResponse(template.render({}, request ))




def index(request):
    yesterday = today - timedelta(days = 1)
    template = loader.get_template('html/listbydates.html')
    context = {
        'mypatients':Appointments.objects.filter(appointment_date=yesterday),
    'doctor':UserDoctor.objects.all(),
        'yesterday': yesterday,
    }
    return HttpResponse(template.render(context, request))


def getdoctor(request):
    return render(request, "html/listbydates.html")


        
def getpatients(request):
    doc= request.GET['doctors']
    yesterday = today - timedelta(days = 1)
    newpatients =  []
    for i in Appointments.objects.all():
        if i.appointment_date==yesterday and i.doctor.user_doctor.last_name==doc:
            newpatients.append(i)
    return render(request,'html/listbydoctor.html', { 'newpatients':newpatients, 'doc':doc})


def lists(request):
    yesterday = today - timedelta(days = 1)
    Doctorlist = UserDoctor.objects.all()
    template = loader.get_template('html/listsforalldoctors.html')
    context = {
        'Appointments': Appointments.objects.filter(appointment_date=yesterday),
        'Doctorlist': Doctorlist,
    }
    return HttpResponse(template.render(context, request))

def checkpriority(request):
    return render(request, "html/checkpriority.html", {})

# fix 
def checkid(request):
    today = date.today()
    patients=[]
    yesterday = today - timedelta(days = 1)
    ident = request.POST['identity']
    for i in UserPatient.objects.all():
        if yesterday == i.user_patient.date_joined.date():
            patients.append(i)
            print(patients)
    
    template = loader.get_template('html/checkid.html')
    context ={
        'patients':patients,
        'ident': ident,
    }
    return HttpResponse(template.render(context, request)) 


def checkdatesofappointments(request):
    cal = HTMLCalendar().formatmonth(today.year, today.month)
    return render(request, 'html/checkdates.html',{"cal": cal,'doc':UserDoctor.objects.all()})
   

def checkdates(request):
    doctor = request.POST['doctor_name']
    dateappointment = request.POST['date']
    appointments_list =[]
    appointments_list1 =[]
    appointments_list = Appointments.objects.filter(appointment_date = dateappointment)
    for item in appointments_list:
        if item.doctor.user_doctor.last_name ==doctor:
            appointments_list1.append(item)
    template = loader.get_template('html/tabledates.html')
    context ={
        'doctor': doctor,
        'appointments_list': appointments_list1,
        'dateappointment':dateappointment,
    }
    return HttpResponse(template.render(context, request))  

def add (request):
    # patients = Patient.objects.all().values()
    # events = Event.objects.all().values()
    return render(request, "html/add.html", {})


def addappointment(request):
    patient_name = request.POST['patient_name']
    patient_identity = request.POST['patient_identity']
    priority = request.POST['priority']
    doctor_name = request.POST['doctor_name']
    appointment_date = request.POST['day']
    start_time= request.POST['start_time']
    end_time = request.POST['end_time']

    flag =False
    for item in Appointments.objects.all():
        if item.start_time != start_time and item.appointment_date != appointment_date:
            flag = True
    Appointment=Appointments()
    if flag:
        for item in Appointments.objects.all():
            if item.patient.user_patient.first_name ==patient_name and item.patient.id_number == patient_identity:
                Appointment.patient =item.patient
                Appointment.patient.id_number== item.patient.id_number
            if item.doctor.user_doctor.last_name ==doctor_name:
                Appointment.doctor =item.doctor
                Appointment.appointment_date = appointment_date
                Appointment.start_time = start_time
                Appointment.end_time = end_time
                Appointment.patient.priority = priority
                Appointment.save()
    else:
         return render(request, 'html/add.html',{})

        
 
    template = loader.get_template('html/contact.html')
    context ={
    'patient_name':patient_name,
    'doctor_name':doctor_name,
    'appointment_date':appointment_date,
    'start_time':start_time,
    }
    return HttpResponse(template.render(context, request))  

def response(request):
    
    return render(request, "html/urgent.html", {'Appointment':Appointments.objects.all()})

def addurgentappointment(request):
    patient_last_name = request.POST['patient_last_name']
    patient_identity = request.POST['patient_identity']
    priority = request.POST['priority']
    doctor_name = request.POST['doctor_name']
    appointment_date = request.POST['day']
    start_time= request.POST['start_time']
    end_time = request.POST['end_time']
    patient_first_name = request.POST['patient_first_name']
    patient_phone_number = request.POST['patient_phone_number']
    patient_email = request.POST['patient_email']
    flag =False
    for item in Appointments.objects.all():
        if item.start_time != start_time and item.appointment_date != appointment_date:
            flag = True
    Appointment=Appointments()
    if flag:
        for item in Appointments.objects.all():
            if item.patient.user_patient.first_name ==patient_first_name and item.patient.id_number == patient_identity:
                Appointment.patient =item.patient
                Appointment.patient.id_number= item.patient.id_number
            if item.doctor.user_doctor.last_name ==doctor_name:
                Appointment.doctor =item.doctor
                Appointment.appointment_date = appointment_date
                Appointment.start_time = start_time
                Appointment.end_time = end_time
                Appointment.patient.user_patient.last_name =patient_last_name
                Appointment.patient.priority = priority
                Appointment.patient.phone_number =patient_phone_number
                Appointment.patient.user_patient.email =patient_email
                Appointment.save()
    else:
        return render(request, 'html/response.html',{'Appointment':Appointments.objects.all()})


 
    template = loader.get_template('html/contact.html')
    context ={
        'patient_name':patient_first_name,
        'doctor_name':doctor_name,
        'appointment_date':appointment_date,
        'start_time':start_time,
    }
    return HttpResponse(template.render(context, request))  
    
    
    



def cancel(request):
    mypatients = Appointments.objects.all()
    template = loader.get_template('html/cancel.html')
    context ={'mypatients':mypatients,}
    return HttpResponse(template.render(context, request)) 

def cancellation(request):
    mydoctor = request.POST['doctor_name']
    mydate = request.POST['date']
    for item  in Appointments.objects.all():
        if item.doctor.user_doctor.last_name == mydoctor:
            if item.appointment_date == datetime.strptime((mydate), "%Y-%m-%d").date():
                item.delete()
    template = loader.get_template('html/cancellationsuccess.html')
    context ={'newpatients':Appointments.objects.all()}
    return HttpResponse(template.render(context, request)) 

def reschedule (request):
    template = loader.get_template('html/reschedule.html')
    context ={'appointments':Appointments.objects.all(),}
    return HttpResponse(template.render(context, request)) 

def rescheduling(request):
    identity = request.POST['identity']
    date = request.POST['date']
    priority = request.POST['priority']
    patient_name = request.POST['patient_name']
    doctor_name = request.POST['doctor_name']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    for item in Appointments.objects.all():
        if item.patient.user_patient.first_name == patient_name:
            if item.doctor.user_doctor.last_name == doctor_name:
                if item.patient.id_number == identity:
                    item.appointment_date = datetime.strptime((date), '%Y-%m-%d').date()
                    item.start_time = datetime.strptime(start_time,"%H:%M").time()
                    item.end_time = datetime.strptime(end_time,"%H:%M").time()
                    item.patient.priority = priority
                    # print(type(item.patient.priority),"  ",type(int(priority)))
                    item.save()
                    template = loader.get_template('html/rescheduler.html')
                    context ={
                    'appointment':Appointments.objects.all(),}
                    return HttpResponse(template.render(context, request))
                    
    template = loader.get_template('html/rescheduler.html')
    context ={
    'appointment':Appointments.objects.all(),}
    return HttpResponse(template.render(context, request)) 

def payment(request):
    today = date.today()
    todayevents = Appointments.objects.filter(appointment_date=today)
    return render(request, "html/payment.html", {'todayevents':todayevents}) 

def confirm(request):
    return render(request,'html/confirm.html', {'listpayment':Appointments.objects.all()})

def tarif(request):
    return render(request,'html/tarif.html')
 

def contacting(request):
    choice = request.POST['doctors']
    return render(request,'html/contact1.html', {'choice':choice})