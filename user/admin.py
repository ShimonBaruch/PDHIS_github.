from django.contrib import admin
from .models import UserSecretary,UserDoctor,UserPatient,Appointments,Document,messege,messegetos,messege_for_patient




# Register your models here.
admin.site.register(UserSecretary)
admin.site.register(UserPatient)
admin.site.register(UserDoctor)
admin.site.register(Appointments)
admin.site.register(Document)
admin.site.register(messege)
admin.site.register(messegetos)
admin.site.register(messege_for_patient)
