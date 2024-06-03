from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_Nurse = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)

class Doctor(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Contact_no = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Specialisation = models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class Nurse(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Contact_no = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Emp_id = models.CharField(max_length=10)

class Patient(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Contact_no = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class pharmacist(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Contact_no = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Emp_id = models.CharField(max_length=10)

class Accessory(models.Model):
    Equipments = models.CharField(max_length=200)

class Request(models.Model):
    user = models.ForeignKey(Patient,on_delete=models.CASCADE)
    request = models.ForeignKey(Accessory,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Doctor_schedule(models.Model):
    Doctor_Name = models.CharField(max_length=100)
    Date = models.DateField()
    Time = models.TimeField()



class Doctor_schedule_booking(models.Model):
    user = models.ForeignKey(Patient,on_delete=models.CASCADE)
    schedule = models.ForeignKey(Doctor_schedule,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Notification(models.Model):
    notification = models.CharField(max_length=255)

class Prescription(models.Model):
    user = models.ForeignKey(Patient,on_delete=models.CASCADE)
    prescription = models.FileField(upload_to='document/')


class Services(models.Model):
    service = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    Date = models.DateField()
    Time = models.TimeField()

class Reports(models.Model):
    Doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Reports = models.FileField(upload_to='document/')
    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE)

class Service_request(models.Model):
    user = models.ForeignKey(Patient,on_delete=models.CASCADE)
    request_service = models.ForeignKey(Services,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
