from django.contrib import admin
from .models import Hospital, Department, Doctor, Patient, Appointment, MedicalRecord,Event

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_details')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'head_of_department', 'hospital')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'contact_details', 'department')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact_details')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_and_time', 'status')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_of_visit', 'diagnosis')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('title','date','user_email')


