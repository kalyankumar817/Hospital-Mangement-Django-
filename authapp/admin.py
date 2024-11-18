from django.contrib import admin
from .models import signupdata,patientdata,appointmentdata


@admin.register(signupdata)
class SignupDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'name')
    search_fields = ('username', 'name')

@admin.register(patientdata)
class PatientDataAdmin(admin.ModelAdmin):
    list_display=('name','age','gender','contact','address')


@admin.register(appointmentdata)
class AppointmentDataAdmin(admin.ModelAdmin):
    list_display=('patient','problem','doctor','date','status','accepted')
    list_filter = ('status', 'accepted')
    search_fields = ('patient__name', 'problem', 'doctor')
    actions = ['approve_appointments', 'decline_appointments']

    @admin.action(description='Approve selected appointments')
    def approve_appointments(self, request, queryset):
        queryset.update(status='Approved', accepted=True)
    
    @admin.action(description='Decline selected appointments')
    def decline_appointments(self, request, queryset):
        queryset.update(status='Declined', accepted=False)
