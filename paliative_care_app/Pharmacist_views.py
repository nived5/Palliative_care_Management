from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from paliative_care_app.filter import PatientFilter
from paliative_care_app.models import Notification, Prescription, Patient

@login_required(login_url='login_view')
def Pharmacist_notification_view(request):
    data = Notification.objects.all()
    return render(request,'Pharmacist templates/Notification_view.html',{'data':data})

# def search_prescription(request,id):
#     global details
#     if request.method == 'GET':
#         data = request.user.get(id=id)
#         details = Prescription.objects.filter(user = data)
#     return render(request,'Pharmacist templates/Search_prescription.html',{'details':details})
@login_required(login_url='login_view')
def prescription_search(request):
    user_list =Prescription .objects.all()
    print(user_list)
    user_filter = PatientFilter(request.GET,queryset =user_list )
    return render(request,'Pharmacist templates/Search_prescription.html',{'filter':user_filter})
