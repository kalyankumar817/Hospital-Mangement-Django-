from django.shortcuts import render,redirect
from .forms import RegisterForm
from.models import signupdata
from .models import patientdata
from .models import appointmentdata
from .forms import LoginForm
from .forms import PatientForm
from .forms import AppointmentForm


# Create your views here.
def loginpage(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            print(f"Attempting login with Username: {username}, Password: {password}")
            #authenticate user
            try:
                user = signupdata.objects.get(username=username, password=password)
                print("User found:", user)
                return render(request, 'home.html')
            except signupdata.DoesNotExist:
                print("User not found")
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
        

def registerpage(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            cus=signupdata.objects.create(name=name,username=username,password=password)
            cus.save()
            return redirect('login')
    else:       #get method
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

def addpatientpage(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            gender=form.cleaned_data['gender']
            contact=form.cleaned_data['contact']
            address=form.cleaned_data['address']

            patient=patientdata.objects.create(name=name,age=age,gender=gender,contact=contact,address=address)
            patient.save()
            return redirect('patients_list')
    else:
        form=PatientForm()
    return render(request,'addpatient.html',{'form':form})


#home page
def homepage(request):
    return render(request,'home.html')

#getting to diaply the patients details
def patientspagelist(request):
    patients=patientdata.objects.all()
    return render(request,'patientlists.html',{'patients':patients})

#display the doctors list
def doctorslist(request):
    return render(request,'doctorlists.html')

#getting the patient details and also  fill the appointment form
def appointmentform(request):
    if request.method=='POST':
        patients=patientdata.objects.all()
        for patient in patients:
            problem = request.POST.get(f'problem_{patient.id}')
            doctor = request.POST.get(f'doctor_{patient.id}')
            date = request.POST.get(f'date_{patient.id}')
            if problem and doctor and date:
                appointmentdata.objects.create(
                    patient=patient,
                    problem=problem,
                    doctor=doctor,
                    date=date
                )
        return render(request,'appointmentfinished.html')
    patients=patientdata.objects.all()
    return render(request,'appointmentdetails.html',{'patients':patients})

def appointmentstatus(request):
    appointments=appointmentdata.objects.all()
    return render(request,'appointmentstatus.html',{'appointments':appointments})
