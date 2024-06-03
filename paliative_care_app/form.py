from django import forms
from django.contrib.auth.forms import UserCreationForm


from paliative_care_app.models import Login, Doctor, Nurse, Patient, pharmacist, Accessory, Doctor_schedule, \
    Notification, Prescription, Services, Reports


class DateInput(forms.DateInput):
    input_type = 'Date'

class TimeInput(forms.TimeInput):
    input_type = 'Time'

class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2')

class Doctor_Form(forms.ModelForm):
      class Meta:
          model = Doctor
          fields = ('Name','Contact_no','Email','Specialisation')

class Nurse_Form(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('Name', 'Contact_no', 'Email', 'Emp_id')

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields =('Name', 'Contact_no', 'Email', 'Address')

class Pharmacist_form(forms.ModelForm):
    class Meta:
        model = pharmacist
        fields = ('Name', 'Contact_no', 'Email', 'Emp_id')

class Accessory_list(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ('Equipments',)

class Doctor_schdule_form(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    Time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Doctor_schedule
        fields = ('Doctor_Name','Date','Time')

class notification_form(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('notification',)

class Prescription_form(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('user','prescription')

class services_form(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    Time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Services
        fields = ('service','Details','Date','Time')


class reports_form(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ('Doctor_name','Reports','patient_name')
