from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from paliative_care_app.models import Request, Patient, Notification, Services


#This function is used for viewing accessory list by  nurse.
@login_required(login_url='login_view')
def Accessory_list_view(request):
    data_1 = Request.objects.all()
    return render(request,'Nurse templates/Accessory_booking_list_view.html',{'data':data_1})
@login_required(login_url='login_view')

def status_change_1(request,id):
    status = Request.objects.get(id=id)
    status.status = 1
    status.save()
    return redirect('Accessory_list_view')
    return render(request,'Nurse templates/Accessory_booking_list_view.html')
@login_required(login_url='login_view')
def status_change_2(request,id):
    status = Request.objects.get(id=id)
    status.status = 1
    status.save()
    return redirect('Accessory_list_view')
    return render(request,'Nurse templates/Accessory_booking_list_view.html')
@login_required(login_url='login_view')
def Nurse_patient_list_view(request):
        data = Patient.objects.all()
        return render(request, 'Nurse templates/Patient_list_view.html', {'data': data})

@login_required(login_url='login_view')
def Nurse_notification_view(request):
    data = Notification.objects.all()
    return render(request,'Nurse templates/Nurse_notification_view.html',{'data':data})


