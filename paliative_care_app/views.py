from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

from paliative_care_app.form import Login_Form, Doctor_Form, Nurse_Form, Patient_form, Pharmacist_form
from paliative_care_app.models import Doctor


# Create your views here.
def testpage(request):
    return render(request,'test.html')

# def dashboard(request):
#     return render(request,'Dashboard.html')

#This function is used to implement dashboard
def dashboard_1(request):
    return render(request,'index.html')

#This function is used to implement landing page of the website
def landing_page(request):
    return render(request,'landingpage.html')

#This function is used to implement login page of the website
def Login_page(request):
    return render(request,'login.html')


#This function is used to Doctor registration
def Doctor_Registration(request):
    form1 = Login_Form()
    form2 =Doctor_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Doctor_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_doctor =True
            user.save()
            user1 = form2.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'registration.html',{'form1':form1,'form2':form2})


#This function is used to Nurse registration
def Nurse_Registration(request):
    form1 = Login_Form()
    form2 =Nurse_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Nurse_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_Nurse = True
            user.save()
            user1 = form2.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'Nurse_Registration.html',{'form1':form1,'form2':form2})


#This function is used to patient registration
def Patient_Registration(request):
    form1 = Login_Form()
    form2 =Patient_form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Patient_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_patient = True
            user.save()
            user1 = form2.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'PatientRegistration.html',{'form1':form1,'form2':form2})

#This function is used to Pharmacist registration
def Pharmacist_Registration(request):
    form1 = Login_Form()
    form2 =Pharmacist_form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Pharmacist_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_pharmacist = True
            user.save()
            user1 = form2.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'Pharmacist_Registration.html',{'form1':form1,'form2':form2})

def doctor_view(request):
    return render(request,'Doctor templates/Doctor_view.html')

def Admin_view(request):
    return render(request,'Admin_templates/Admin_page.html')

def Nurse_page(request):
    return render(request,'Nurse templates/Nusre _page.html')


def Patient_page(request):
    return render(request,'Patient templates/Patient_view.html')

def Pharmacist_view(request):
    return render(request,'Pharmacist templates/Pharmacist_view.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            # print(user)
            login(request,user)
            print('hii')
            print(user)
            if user.is_staff:
                return redirect('Admin_view')
            elif user.is_doctor:
                return redirect('doctor_view')
            elif user.is_Nurse:
                return redirect('Nurse_page')
            elif user.is_pharmacist:
                return redirect('Pharmacist_view')
            elif user.is_patient:
                return redirect('Patient_page')
        else:
            messages.info(request,'Invalid credentials ')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')
