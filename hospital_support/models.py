from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Hospital(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_details = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Department(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    head_of_department = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True,related_name="department_doctor")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Doctor(BaseModel):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=10)
    department = models.ForeignKey(Department,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Patient(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact_details = models.CharField(max_length=10)
    medical_history = models.TextField()
    insurance_information = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    reason_for_appointment = models.TextField()
    status = models.CharField(max_length=20, default='Scheduled')

    def __str__(self):
        return f"{self.patient.name} - {self.date_and_time}"

class MedicalRecord(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_of_visit = models.DateField()
    diagnosis = models.TextField()
    prescribed_medications = models.TextField()
    treatment_details = models.TextField()

    def __str__(self):
        return f"Medical record for {self.patient.name}"

# Add more models as needed (e.g., Nurse, Medication, Billing, Room, Bed, Surgery, LabTest, etc.)

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    user_email = models.EmailField()

    def __str__(self):
        return self.title

