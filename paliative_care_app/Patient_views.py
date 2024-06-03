from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from paliative_care_app.form import reports_form
from paliative_care_app.models import Accessory, Patient, Request, Doctor_schedule, Doctor_schedule_booking, \
    Prescription, Reports, Services, Service_request, Notification


#This function is used for requesting equipments added by admin.
@login_required(login_url='login_view')
def RequestForAccessories(request,id):
    data = Accessory.objects.get(id=id)
    # print(request.user)
    u = Patient.objects.get(user=request.user)
    # print("hai")
    # print(u)
    booking = Request.objects.filter(user = u,request =data )
    if booking.exists():
        messages.info(request,'you have requested for accessories')
        return redirect('patient_accessory_view')
    else:
        if request.method == 'POST':
            obj = Request()
            obj.user = u
            obj.request = data
            obj.save()
            messages.info(request,'Requested successfully')
            return redirect('/')
        return render(request,'Patient templates/Accessory_request.html',{'data':data})

#This function is used for accessory list view.
@login_required(login_url='login_view')
def patient_accessory_view(request):
    data = Accessory.objects.all()
    return render(request,'Patient templates/Patient_accessory_view.html',{'data':data})

@login_required(login_url='login_view')
def Accessory_confirmation_list(request):
    user_1 = request.user
    patient_1 = Patient.objects.get(user=user_1)
    # print(patient_1)
    data = Request.objects.filter(user = patient_1)
    return  render(request,'Patient templates/Accssry_confirmation_list.html',{'data':data})
@login_required(login_url='login_view')
def Patient_Doctor_schedule_view(request):
    data = Doctor_schedule.objects.all()
    return render(request,'Patient templates/Patient_Doctor_schedule_view.html',{'data':data})
@login_required(login_url='login_view')
def Doctor_Appointment(request,id):
    data = Doctor_schedule.objects.get(id=id)
    print(data)
    u = Patient.objects.get(user=request.user)
    booking = Doctor_schedule_booking.objects.filter(user = u,schedule =data )
    print(booking)
    if booking.exists():
        messages.info(request,'you have requested for Doctor appoitnment')
        return redirect('Patient_Doctor_schedule_view')
    else:
        if request.method == 'POST':
            obj = Doctor_schedule_booking()
            obj.user = u
            obj.schedule = data

            obj.save()
            messages.info(request,'Requested successfully')
            print(data)
            return redirect('/')
        return render(request,'Patient templates/Appoinment_booking.html',{'data':data})

@login_required(login_url='login_view')
def Doctor_Booking_confirmation_list(request):
    user_1 = request.user
    patient_1 = Patient.objects.get(user=user_1)
    # print(patient_1)
    data = Doctor_schedule_booking.objects.filter(user = patient_1)
    return  render(request,'Patient templates/Appointment_confirmation.html',{'data':data})
@login_required(login_url='login_view')
def View_prescription(request):
    data = Prescription.objects.all()
    return render(request,'Patient templates/Prescription_view.html',{'data':data})

@login_required(login_url='login_view')
def send_reports(request):
        form = reports_form()
        #  print(form)
        if request.method == 'POST':
            data = reports_form(request.POST, request.FILES)
            # print(data)
            if data.is_valid():
                data.save()
            return redirect('view_reports')
        return render(request, 'Patient templates/Add_reports.html', {'form': form})


@login_required(login_url='login_view')
def view_reports(request):
    data = Reports.objects.all()
    return render(request,'Patient templates/Patient_reports_view.html',{'data':data})
@login_required(login_url='login_view')
def view_Services(request):
    data = Services.objects.all()
    return render(request,'Patient templates/Patient_service_view.html',{'data':data})
@login_required(login_url='login_view')
def Request_for_services(request,id):
    data = Services.objects.get(id=id)
    u = Patient.objects.get(user=request.user)
    booking = Service_request.objects.filter(user = u,request_service=data)
    if booking.exists():
        messages.info(request,'you have requested for service')
        return redirect('view_Services')
    else:
      if request.method == 'POST':
        obj = Service_request()
        obj.user =u
        obj.request_service=data
        obj.save()
        messages.info(request, 'Requested successfully')
        return redirect('/')
    return render(request, 'Patient templates/Requesting_for_services.html', {'data': data})

@login_required(login_url='login_view')
def service_request_confirmation_list(request):
    user_1 = request.user
    patient_1 = Patient.objects.get(user=user_1)
    print(patient_1)
    data = Service_request.objects.filter(user= patient_1)
    print(data)
    return render(request,'Patient templates/Serive_confirmation_list.html',{'data':data})
@login_required(login_url='login_view')
def Patient_notification_view(request):
    data = Notification.objects.all()
    return render(request,'Patient templates/Patient_notification_view.html',{'data':data})