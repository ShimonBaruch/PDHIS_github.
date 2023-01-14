from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django import forms




class UserSecretary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField( max_length=10, blank=False) 
    email = models.EmailField()
    Role =models.CharField(max_length=50,choices=(('1','secretary'),('2','secretary'),('1','secretary')), default='Secretary')
    

    def __str__(self):
        return self.user.username

class UserPatient(models.Model):
    user_patient = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=9)
    phone_number =models.CharField(max_length=10)
    Role = models.CharField(max_length=1, choices=(('1', 'patient'),('1', 'patient')), default='patient')
    priority = models.IntegerField(default=1,blank=True)
   
    # def fname(self):
    #     return self.user_patient.first_name
    # def lname(self):
    #     return self.user_patient.last_name
    # def phone(self):
    #     return self.user_patient.phone_number
    # def identity(self):
    #     return self.user_patient.id_number
    # def date_created(self):
    #     return self.user_patient.date_joined.date
    # def email(self):
    #     return self.user_patient.email
    # def priority(self):
    #     return self.user_patient.priority
    # def __str__(self):
    #     return self.user_patient.username


 
class UserDoctor(models.Model):
    user_doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    Role = models.CharField(max_length=1, choices=(('1', 'doctor'),('1', 'doctor')), default='doctor')
    department = models.CharField(max_length=50, choices = (('1','Otorhinolaryngology'),('2', 'Cardiology'),('3','Oncology'),('4','Dermatologist'),('5','Endocrinologist'),('6','Gastroenterologist'),('7','Hematologist'),('8','Nephrologists'),('9','Neurologists'),('10','Ophthalmologist')))
    rate = models.IntegerField(default=1,blank=True)

    def __str__(self):
        return self.user_doctor.username

    def get_value(self):
        value =self.department
        return self
class messege(models.Model):
    patient = models.ForeignKey(UserPatient,on_delete = models.PROTECT)
    doctor = models.ForeignKey(UserDoctor,on_delete = models.PROTECT)
    messege =models.TextField(null=True,blank=True)
       
class messegetos(models.Model):
    doctor = models.ForeignKey(UserDoctor,on_delete = models.PROTECT)
    secretary = models.ForeignKey(UserSecretary,on_delete = models.PROTECT)
    messege =models.TextField(null=True,blank=True)

class messege_for_patient(models.Model):
    patient = models.ForeignKey(UserPatient,on_delete = models.PROTECT)
    secretary = models.ForeignKey(UserSecretary,on_delete = models.PROTECT)
    messege =models.TextField(null=True,blank=True)

class Appointments(models.Model):
    patient = models.ForeignKey(UserPatient,on_delete = models.PROTECT)
    doctor = models.ForeignKey(UserDoctor,on_delete = models.PROTECT)
    appointment_date = models.DateField(default=date.today)
    start_time = models.TimeField(blank=False)
    end_time =models.TimeField(blank=False)
    appointment_end = models.BooleanField(default=False)
    summary=models.TextField(null=True,blank=True)
    patient_payment = models.IntegerField(null=True,default=0)
    payment_file = models.FileField(name='payment_file',null=True,blank=True,upload_to='uploads')
    medical_file = models.FileField(name='medical_file', null=True,blank=True,upload_to='uploads')
    # def fname(self):
    #     return self.A.patient.user_patient.first_name
    # def lname(self):
    #     return self.A.patient.user_patient.last_name
    # def identity(self):
    #     return self.A.patient.id_number
    # def phone(self):
    #     return self.A.patient.phone_number
    # def email(self):
    #     return self.A.patient.email
    # def date_created(self):
    #     return self.A.patient.user_patient.date_joined.date
    # def date_appointment(self):
    #     return self.A.appointment_date
    # def priority(self):
    #     return self.A.patient.priority
    # def doctor(self):
    #     return self.A.doctor.user_doctor.last_name

    
class Document(models.Model):
    Document = models.FileField(upload_to='uploads')



# class UploadFileForm(forms.ModelForm):
#     appointment = models.OneToOneField(Appointments,on_delete = models.PROTECT)
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

