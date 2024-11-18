from django.db import models

# Create your models here.
class signupdata(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class patientdata(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)  # Updated max_length to 6
    contact = models.CharField(max_length=15)  # CharField to handle phone numbers
    address = models.CharField(max_length=255)

class appointmentdata(models.Model):
    patient=models.ForeignKey(patientdata,on_delete=models.CASCADE)
    problem=models.CharField(max_length=255)
    doctor=models.CharField(max_length=255)
    date=models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending')
    accepted = models.BooleanField(default=False)  # Added field for acceptance