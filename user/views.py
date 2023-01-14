
from django.shortcuts import render,redirect
from .forms import CustomRegisterForm 
from .forms import CustomRegisterForm 
from django.contrib import messages
from .forms import UserPatientForm,UserDoctorForm,CustomRegisterForm
from user.models import UserDoctor,Appointments,UserPatient,UserSecretary
from django.contrib import messages
from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect

# from secretary.views import homemsecretary

#from .forms import CustomRegisterForm ,UserPatientForm
#Create your views here.



def register(request):
    
    if request.method=="POST":
        register_form =CustomRegisterForm(request.POST) 
        profile_form = UserPatientForm(request.POST)
        if register_form.is_valid() and profile_form.is_valid() :
            user = register_form.save()
            profile = profile_form.save(commit=False)
            profile.user_patient = user
            profile.save()
            messages.success(request,("Welcome, login to start"))
            return redirect('login_request')

    else:
        register_form = CustomRegisterForm()
        profile_form = UserPatientForm()
    context ={'register_form' : register_form ,'profile_form': profile_form,'ok1':False}
    return render(request,'register.html',context)


# def doctor_register(request):
#     if request.method=="POST":
#         register_form =CustomRegisterForm(request.POST) 
#         profile_doctor_form = UserDoctorForm(request.POST)
#         if register_form.is_valid() and profile_doctor_form.is_valid() :
#             user = register_form.save()
            
#             profile = profile_doctor_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             messages.success(request,("Welcome Doctor, login to start"))
#             return redirect('login')

#     else:
#         register_form = CustomRegisterForm()
#         profile_doctor_form = UserDoctorForm()
#     context ={'register_form' : register_form ,'profile_doctor_form': profile_doctor_form}
#     return render(request,'doctor_register.html',context)
@csrf_protect
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, "You are now logged in as "+ username +" ")
            if user is not None:
                for i in UserPatient.objects.all():
                    if i.user_patient.username  == username :
                        
                        app =Appointments.objects.filter(patient=i)
                        num=len(app)
                        context ={'num':num}
                        return redirect('patient_home')
                for i in UserDoctor.objects.all():
                    if i.user_doctor.username == username :
                        return redirect('hpage')
                for i in UserSecretary.objects.all():
                    if i.user.username == username :
                        return redirect('medicalsecretary_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,template_name='login.html',context={"form":form})