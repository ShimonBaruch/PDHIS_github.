from django import forms
from django.contrib.auth.forms import UserCreationForm ,User
from .models import UserSecretary,UserPatient,UserDoctor,Appointments,messege,messegetos,messege_for_patient
from django.forms import SelectDateWidget
from datetime import date







    # appointment = models.ForeignKey(Appointments, on_delete = models.PROTECT)
    # payment_file = models.FileField(name='payment_file',null=True,blank=True)
    # medical_file = models.FileField(name='medical_file', null=True,blank=True)

class CustomRegisterForm(UserCreationForm):

    class Meta:
        model= User
        fields = ['username','email','first_name','last_name','password1','password2']
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserSecretary
        fields = ['Role']
        
 
class UserPatientForm(forms.ModelForm):
    
    class Meta:
        model= UserPatient
        fields = ['id_number','phone_number']

    def clean_id_number(self):

        ID=self.cleaned_data['id_number']
        if(len(ID)!=9):
            raise forms.ValidationError("Invalid id number[id number must contain 9 digits]")

        if(ID.isdigit()==False):
            raise forms.ValidationError("Invalid id number[only numbers are allowed]")
        return ID

    def clean_phone_number(self):
        PHONE=self.cleaned_data['phone_number']
        if(len(PHONE)!=10):
            raise forms.ValidationError("Invalid phone number[phone number must be 10 digits]")
        if(PHONE[0] !='0' or PHONE[1] !='5'):
            raise forms.ValidationError("Invalid phone number[format:05X-XXX-XXXX]")
        
        if(PHONE.isdigit() == False):
            raise forms.ValidationError("Invalid phone number[phone number must be 10 digits]")
        return PHONE


class UserDoctorForm(forms.ModelForm):
    class Meta:
        model=UserDoctor
        fields = ['Role','department']

class AppointmentsForm(forms.ModelForm):
    class Meta():
        model = Appointments
        fields = ['appointment_date','start_time']
        widgets = {
            'appointment_date': SelectDateWidget(years=range(2023, date.today().year + 2)),
        }
class patient_messege_form(forms.ModelForm):
    class Meta:
        model = messege
        fields = ['messege','doctor',]
        
class patient_to_secretary_form(forms.ModelForm):
    class Meta:
        model = messege_for_patient
        fields = ['messege','secretary',]

class doctor_messege_form(forms.ModelForm):
    class Meta:
        model = messegetos
        fields = ['messege','secretary',]
        

class Appointments_Form(forms.ModelForm):
   
    class Meta():
        model = Appointments
        fields = ['appointment_date','start_time','payment_file','medical_file',]
       
