from django.shortcuts import render, redirect

from paliative_care_app.form import Accessory_list, Doctor_schdule_form, notification_form, services_form
from paliative_care_app.models import Doctor, Nurse, Patient, pharmacist, Accessory, Doctor_schedule, Notification, \
    Services


#This function is used for view doctor page by admin .
def Admin_Doctor_view(request):
    data = Doctor.objects.all()
    return render(request,'Admin_templates/Admin_doctorlist_view.html',{'data':data})


# This function is used for view nurse page by admin .
def Admin_Nurse_view(request):
    data = Nurse.objects.all()
    return render(request,'Admin_templates/Admin_Nurse_view.html',{'data':data})

#This function is used for view patient page by admin .
def Admin_Patient_view(request):
    data = Patient.objects.all()
    return render(request,'Admin_templates/Admin_Patient_view.html',{'data1':data})

#This function is used for view pharmacist page by admin .
def Admin_pharmacist_view(request):
    data = pharmacist.objects.all()
    return render(request,'Admin_templates/Admin_pharmacist_view.html',{'data':data})

#This function is used for adding accessory by admin.
def AddAccessories(request):
    form = Accessory_list()
    if request.method == 'POST':
        data = Accessory_list(request.POST)
        if data.is_valid():
            data.save()
        return redirect('AddAccessories')
    return render(request,'Admin_templates/Add_accessory.html',{'form':form})


#This function is used for view the accessory list.
def AdminAccessoryView(request):
    data = Accessory.objects.all()
    return  render(request,'Admin_templates/Admin_accessory_view.html',{'data':data})

#This function is used for deleting accessory from accessory list.
def delete_accessory(request,id):
    data = Accessory.objects.get(id=id)
    data.delete()
    return redirect('AdminAccessoryView')


def Add_doctor_Schedule(request):
    form = Doctor_schdule_form()
    if request.method == 'POST':
        data = Doctor_schdule_form(request.POST)
        if data.is_valid():
            data.save()
        return redirect('Add_doctor_Schedule')
    return render(request,'Admin_templates/Add_doctor_schedule.html',{'form':form})

def Admin_Doctor_schedule_view(request):
    data = Doctor_schedule.objects.all()
    return render(request,'Admin_templates/Admin_Doctor_schdule_view.html',{'data':data})

def delete_Doctor_schedule(request,id):
    data = Doctor_schedule.objects.get(id=id)
    data.delete()
    return redirect('Admin_Doctor_schedule_view')

def Add_notification(request):
    form = notification_form()
    if request.method == 'POST':
        data = notification_form(request.POST)
        if data.is_valid():
            data.save()
        return redirect('Admin_notification_View')
    return render(request,'Admin_templates/Add_notification.html',{'form':form})


def Admin_notification_View(request):
    data = Notification.objects.all()
    return  render(request,'Admin_templates/Admin_notification_view.html',{'data':data})

def AddServices(request):
    form = services_form()
    if request.method == 'POST':
        data = services_form(request.POST)
        if data.is_valid():
            print("hai")

            data.save()
        return redirect('Admin_Service_view')
    return render(request,'Admin_templates/Add_services.html',{'form':form})


def Admin_Service_view(request):
    data = Services.objects.all()
    return render(request,'Admin_templates/Admin_services_view.html',{'data':data})