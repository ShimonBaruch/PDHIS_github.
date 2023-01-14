from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import UserDoctor,Appointments,UserPatient,User,messege,UserSecretary,messege_for_patient
from user.forms import AppointmentsForm ,patient_to_secretary_form
from django.contrib import messages
from datetime import datetime,timedelta
from django import forms
from django.core.files.storage import FileSystemStorage
# from user.views import login_request
from user.forms import Appointments_Form,AppointmentsForm,patient_messege_form,patient_to_secretary_form
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

 
# Create your views here.
def pages(request):
    context= { 'home_text':"We emphasize the connection between patient and doctor"}
    return render(request,'html/home.html',context)

def about(request):
    context= { 'about_text':"The Motivation Behind - PDHIS"}
    return render(request,'html/about.html',context)

def patient(request):
    context= { 'p_text':"welcome choose from the following"}
    return render(request,'html/patient.html',context)
    
@login_required
def patient_home(request):
    date = None
    for item in User.objects.all():
        if item.username==request.user.username :
            date =item.date_joined.date
    context= {'patient_home_text':"welcome",'date':date}
    return render(request,'html/patient_home.html',context)
@login_required  
def view_appointments(request):
    context= {'patient_home_text':"welcome",'Appointment':Appointments.objects.all()}
    return render(request,'html/view_appointments.html',context)
@login_required  
def medical_files(request):
    Appointment=Appointments.objects.all()
    if request.method == 'POST':
        form =Appointments_Form(request.POST)
        if form.is_valid():
            user = UserPatient.objects.get(user_patient__username=request.user)
            app =Appointments.objects.get(patient=user,appointment_date=form.data['appointment_date'],start_time=form.data['start_time'])
            app.payment_file = request.FILES['payment_file']
            app.medical_file=request.FILES['medical_file']
            app.save()
            return render(request,'html/patient_home.html')
    context= { 'madicl_files_text':"welcome choose from the following",'Appointments_Form':Appointments_Form,'Appointment':Appointment}
    return render(request,'html/medical_files.html',context)

# app =Appointments.objects.all()
#     files =[x.payment_file for x in app]
#     print(len(files))

# {% for file in files %}
# {% csrf_token %}
# {% if file %}
# <object data="{{file.url}}" type="application/pdf" width="100%" height="500px">
#   <p>It appears you don't have a PDF plugin for this browser.
#   No biggie... you can <a href="{{ file.url }}">click here to
#   download the PDF file.</a></p>
# </object>
# {% endif %}
# {% endfor %}
@login_required 
def appointments(request):
    patients = UserPatient.objects.all()
    UserPatientOrNot =False
    patient = request.user.username
    for i in patients:
        if patient == str(i.user_patient.username):
            UserPatientOrNot=True
    context= { 'appointments_text':"welcome choose from the following",'UserPatientOrNot':UserPatientOrNot,'index':False}
    return render(request,'html/Appointments.html',context)

    
@login_required   
def urgent_appeal(request):
    form =patient_messege_form()
    context= { 'urgent_appeal_text':"welcome choose from the following",'form':form}
    return render(request,'html/urgent_appeal.html',context)
@login_required  
def messege_to_patient(request):
    form =patient_messege_form(request.POST)
    doc = UserDoctor.objects.get(id=form.data['doctor'])
    messege_ =messege()
    messege_.messege = form.data['messege']
    messege_.doctor =UserDoctor.objects.get(id=form.data['doctor'])
    messege_.patient = UserPatient.objects.get(user_patient__username= request.user)
    messege_.save()
    context= {'patient_home_text':"welcome"}
    return render(request,'html/patient_home.html',context)

@login_required  
def messegetoseretary(request):
    form = patient_to_secretary_form()
    context= { 'urgent_appeal_text':"welcome choose from the following",'form':form}
    return render(request,'html/messegetosecretary.html',context)
@login_required  
def messegetoseretary2(request):
    form =patient_to_secretary_form(request.POST)
    sec = UserSecretary.objects.get(id=form.data['secretary'])
    messege_ =messege_for_patient()
    messege_.messege = form.data['messege']
    messege_.secretary =UserSecretary.objects.get(id=form.data['secretary'])
    messege_.patient = UserPatient.objects.get(user_patient__username= request.user)
    messege_.save()
    context= { 'urgent_appeal_text':"welcome choose from the following"}
    return render(request,'html/patient_home.html',context)


@login_required   
def create_appointments(request):
    doctype       = request.GET.get('myselect')
    alldocs       = UserDoctor.objects.filter(department__iexact=doctype)
    Appointments__Form=AppointmentsForm()
    patient =UserPatient.objects.get(user_patient__username=request.user)
    patient2=Appointments.objects.get(patient=patient)
    print(patient2)

    alldocs={}
    if request.method == 'GET' and request.GET.get('myselect') != None:
        doctype       = request.GET.get('myselect')
        alldocs       = UserDoctor.objects.filter(department__iexact=doctype)
        Appointments__Form=AppointmentsForm()
        return render(request,'html/create_appointments.html',{'alldocs':alldocs,'Appointments__Form':Appointments__Form,'patient':patient2})


    elif request.method == 'POST':
        patient =UserPatient.objects.get(user_patient__username=request.user)
        Chosen_Doctor=request.POST.get('Chosen_Doctor')
        Chosen_Doctor =UserDoctor.objects.get(user_doctor__username=Chosen_Doctor)
        start = datetime.strptime(request.POST.get('start_time'),"%H:%M:%S").time()
        end = datetime.combine(datetime.today(), start) + timedelta(minutes=15)
        app = Appointments()
        app.patient = patient
        app.doctor = Chosen_Doctor
        appdate = (request.POST.get('appointment_date_month'),request.POST.get('appointment_date_day'),request.POST.get('appointment_date_year'))
        x = "-".join(appdate)
        temp =datetime.strptime((x), "%m-%d-%Y").date()
        for i in Appointments.objects.filter(patient=patient):
            if i.appointment_date == temp and i.start_time ==start:
                context ={'create_appointments_text':'You already have an appointment on this date and time.[see "view appointments"]','alldocs':alldocs,'Appointments__Form':Appointments__Form}
                return render(request,'html/create_appointments.html',context)
                
        app.appointment_date = datetime.strptime((x), "%m-%d-%Y")
        app.start_time = start
        app.end_time = end
        app.save()
        messages.success(request,("New Appointment Created Successfully"))
        return redirect('appointments')
        
    return render(request,'html/create_appointments.html')

@login_required   
def appointment_delete(request):
    app = Appointments.objects.all()
    if request.method == 'GET':
        option = request.GET.get('selectapp')
        pop_up_a = request.GET.get('pop_up_a')
        pop_up_delete = request.GET.get('pop_up_delete')
        if pop_up_delete == None:
            return render(request,'html/appointment_delete.html',{'app':app,'option':option,'pop_up_a':pop_up_a})

        
        if option!=None or pop_up_delete !=None:
            for item in Appointments.objects.all():
               if str(item) == pop_up_delete:
                    item.delete()
                    messages.success(request,("Appointment Deleted Successfully"))
                    return redirect('appointments')   
    return render(request,'html/appointment_delete.html',{'app':app,'option':option,'pop_up_a':pop_up_a})
@login_required  
def update_appointment(request):
    app = Appointments.objects.all()
    if request.method == 'GET':
        option = request.GET.get('selectapp')
        date = request.GET.get('date')
        time = request.GET.get('time')
        if  date == '' or time == '':
            return render(request,'html/update_appointment.html',{'app':app,'update_appointment_text':"You must complete all fields"})
        for item in Appointments.objects.all():
            if str(item)==option:   
                temp1 =datetime.strptime((date), "%Y-%m-%d")
                temp2 =datetime.strptime(time,"%H:%M").time()
                for i in Appointments.objects.all():
                    if item.patient == i.patient:
                        if item.appointment_date != i.appointment_date:
                            print(i.start_time," ",temp2,"==",i.appointment_date,"==",temp1.date())
                            if i.start_time == temp2 and i.appointment_date == temp1.date(): 
                                return render(request,'html/update_appointment.html',{'app':app,'update_appointment_text2':"You already have an appointment on this date and time"})
                item.appointment_date = datetime.strptime((date), "%Y-%m-%d")
                item.start_time = datetime.strptime(time,"%H:%M").time()
                item.save()
                messages.success(request,("Appointment Updated Successfully"))
                return redirect('appointments')  
            


    return render(request,'html/update_appointment.html',{'app':app})

               


    

