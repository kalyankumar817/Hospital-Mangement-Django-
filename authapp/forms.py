from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=50,required=True)
    username=forms.CharField(max_length=50,required=True)
    password=forms.CharField(max_length=50,required=True)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,required=True)
    password=forms.CharField(max_length=50,required=True)

class PatientForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.CharField(max_length=6, required=True)  # Ensure max_length matches the model
    contact = forms.CharField(max_length=15, required=True)  # CharField to handle phone numbers
    address = forms.CharField(max_length=255, required=True)

class AppointmentForm(forms.Form):
    problem=forms.CharField(max_length=255)
    doctor=forms.CharField(max_length=255)
    date=forms.DateField()