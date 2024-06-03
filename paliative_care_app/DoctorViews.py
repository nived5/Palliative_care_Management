from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from paliative_care_app.form import Prescription_form
from paliative_care_app.models import Doctor, Doctor_schedule, Doctor_schedule_booking, Patient, Prescription, \
    Notification, Reports, Services, Service_request


@login_required(login_url='login_view')
def delete_doctor(request,id):
    data = Doctor.objects.get(id=id)
    data.delete()
    return redirect('Admin_Doctor_view')

@login_required(login_url='login_view')
def Doctor_schedule_view(request):
    data = Doctor_schedule.objects.all()
    return render(request,'Doctor templates/Doctor_view_schedule.html',{'data':data})
@login_required(login_url='login_view')
def Appoinment_view(request):
    data = Doctor_schedule_booking.objects.all()
    return render(request,'Doctor templates/Doctor_Booking_list.html',{'data':data})
@login_required(login_url='login_view')
def status_change_1(request,id):
    status = Doctor_schedule_booking.objects.get(id=id)
    status.status = 1
    status.save()
    return redirect('Doctor_Booking_confirmation_list')
    return render(request,'Doctor templates/Doctor_Booking_list.html')
@login_required(login_url='login_view')
def status_change_2(request,id):
    status = Doctor_schedule_booking.objects.get(id=id)
    status.status = 2
    status.save()
    return redirect('Doctor_Booking_confirmation_list')
    return render(request,'Doctor templates/Doctor_Booking_list.html')
@login_required(login_url='login_view')
def Patent_view(request):
    data = Patient.objects.all()
    return render(request,'Doctor templates/Patient_list_view.html',{'data':data})
@login_required(login_url='login_view')
def Add_prescription(request):
    form = Prescription_form()
  #  print(form)
    if request.method == 'POST':
        data = Prescription_form(request.POST,request.FILES)
       # print(data)
        if data.is_valid():
            data.save()
        return redirect('prescription_view')
    return render(request,'Doctor templates/Add_prescription.html',{'form':form})

@login_required(login_url='login_view')
def prescription_view(request):
    data = Prescription.objects.all()
    return render(request,'Doctor templates/Prescription_view.html',{'data':data})
@login_required(login_url='login_view')
def Notification_view(request):
    data = Notification.objects.all()
    return render(request,'Doctor templates/Doctor_notification_view.html',{'data':data})

@login_required(login_url='login_view')
def Reports_view(request):
    data = Reports.objects.all()
    return render(request,'Doctor templates/doctor_Report_view.html',{'data':data})
@login_required(login_url='login_view')
def Services_view_list(request):
    data = Services.objects.all()
    return render(request,'Doctor templates/Doctor_services_view.html',{'data':data})
@login_required(login_url='login_view')
def Service_status_change_1(request,id):
    status = Service_request.objects.get(id=id)
    status.status = 1
    status.save()
    return redirect('/')
    return render(request,'Doctor templates/Doctor_services_view.html')
@login_required(login_url='login_view')
def service_status_change_2(request,id):
    status = Service_request.objects.get(id=id)
    status.status = 1
    status.save()
    return redirect('/')
    return render(request,'Doctor templates/Doctor_services_view.html')


