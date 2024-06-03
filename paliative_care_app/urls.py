from django.urls import path

from paliative_care_app import views, Admin_views, DoctorViews, Patient_views, Nurse_views, Pharmacist_views

urlpatterns = [

    path('',views.landing_page,name='landing_page'),
    # path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard',views.dashboard_1,name='dashboard_1'),
    path('Login_page',views.Login_page,name='Login_page'),
    path('Doctor_Registration',views.Doctor_Registration,name='Doctor_Registration'),
    path('Nurse_Registration',views.Nurse_Registration,name='Nurse_Registration' ),
    path('Patient_Registration',views.Patient_Registration,name='Patient_Registration'),
    path('Pharmacist_Registration',views.Pharmacist_Registration,name='Pharmacist_Registration'),
    path('doctor_view',views.doctor_view,name='doctor_view'),
    path('Admin_view', views.Admin_view, name='Admin_view'),
    path('Nurse_page', views.Nurse_page, name='Nurse_page'),
    path('Patient_page', views.Patient_page, name='Patient_page'),
    path('Pharmacist_view', views.Pharmacist_view, name='Pharmacist_view'),
    path('login_view',views.login_view,name = 'login_view'),
    path('delete_doctor/<int:id>/',DoctorViews.delete_doctor,name='delete_doctor'),
    path('logout_view', views.logout_view, name='logout_view'),

    #Admin urls

    path('Admin_Doctor_view',Admin_views.Admin_Doctor_view,name = 'Admin_Doctor_view'),
    path('Admin_Nurse_view',Admin_views.Admin_Nurse_view,name ='Admin_Nurse_view'),
    path('Admin_Patient_view',Admin_views.Admin_Patient_view,name='Admin_Patient_view'),
    path('Admin_pharmacist_view', Admin_views.Admin_pharmacist_view, name='Admin_pharmacist_view'),
    path('AddAccessories',Admin_views.AddAccessories,name='AddAccessories'),
    path('AdminAccessoryView',Admin_views.AdminAccessoryView,name='AdminAccessoryView'),
    path('delete_accessory/<int:id>/',Admin_views.delete_accessory,name='delete_accessory'),
    path('Add_doctor_Schedule',Admin_views.Add_doctor_Schedule,name='Add_doctor_Schedule'),
    path('Admin_Doctor_schedule_view',Admin_views.Admin_Doctor_schedule_view,name='Admin_Doctor_schedule_view'),
    path('Add_notification',Admin_views.Add_notification,name = 'Add_notification'),
    path('Admin_notification_View',Admin_views.Admin_notification_View,name='Admin_notification_View'),
    path('AddServices',Admin_views.AddServices,name='AddServices'),
    path('Admin_Service_view',Admin_views.Admin_Service_view,name='Admin_Service_view'),



 #Patient url

    path('RequestForAccessories/<int:id>/',Patient_views.RequestForAccessories,name='RequestForAccessories'),
    path('patient_accessory_view',Patient_views.patient_accessory_view,name='patient_accessory_view'),
    path('Accessory_confirmation_list',Patient_views.Accessory_confirmation_list,name='Accessory_confirmation_list'),
    path('Patient_Doctor_schedule_view',Patient_views.Patient_Doctor_schedule_view,name='Patient_Doctor_schedule_view'),
    path('Doctor_Appointment/<int:id>/',Patient_views.Doctor_Appointment,name='Doctor_Appointment'),
    path('Doctor_Booking_confirmation_list',Patient_views.Doctor_Booking_confirmation_list,name = 'Doctor_Booking_confirmation_list'),
    path('View_prescription',Patient_views.View_prescription,name='View_prescription'),
    path('send_reports',Patient_views.send_reports,name = 'send_reports'),
    path('view_reports',Patient_views.view_reports,name = 'view_reports'),
    path('view_Services',Patient_views.view_Services,name='view_Services'),
    path('Request_for_services/<int:id>/',Patient_views.Request_for_services,name = 'Request_for_services'),
    path('service_request_confirmation_list',Patient_views.service_request_confirmation_list,name = 'service_request_confirmation_list'),
    path('Patient_notification_view',Patient_views.Patient_notification_view,name = 'Patient_notification_view'),


 #Nurse url
    path('Accessory_list_view',Nurse_views.Accessory_list_view,name='Accessory_list_view'),
    path('status_change_1/<int:id>/',Nurse_views.status_change_1,name='status_change_1'),
    path('status_change_2/<int:id>/',Nurse_views.status_change_2,name='status_change_2'),
    path('Nurse_patient_list_view',Nurse_views.Nurse_patient_list_view,name='Nurse_patient_list_view'),
    path('Nurse_notification_view',Nurse_views.Nurse_notification_view,name='Nurse_notification_view'),






# Doctor urls
    path('Doctor_schedule_view',DoctorViews.Doctor_schedule_view,name='Doctor_schedule_view'),
    path('Appoinment_view',DoctorViews.Appoinment_view,name='Appoinment_view'),
    path('status_change_1/<int:id>/',DoctorViews.status_change_1,name = 'status_change_1'),
    path('status_change_2/<int:id>/',DoctorViews.status_change_2,name='status_change_2'),
    path('Doctor_Patient_view',DoctorViews.Patent_view,name='Doctor_Patient_view'),
    path('Add_prescription',DoctorViews.Add_prescription,name = 'Add_prescription'),
    path('prescription_view',DoctorViews.prescription_view,name='prescription_view'),
    path('Notification_view',DoctorViews.Notification_view,name='Notification_view'),
    path('Reports_view',DoctorViews.Reports_view,name = 'Reports_view'),
    path('Services_view_list',DoctorViews.Services_view_list,name= 'Services_view_list'),
    path('Service_status_change_1/<int:id>/',DoctorViews.Service_status_change_1,name='Service_status_change_1'),
    path('Service_status_change_2/<int:id>/',DoctorViews.service_status_change_2,name='Service_status_change_2'),



#pharmacist url
    path('Pharmacist_notification_view',Pharmacist_views.Pharmacist_notification_view,name='Pharmacist_notification_view'),
    path('prescription_search',Pharmacist_views.prescription_search,name='prescription_search'),


]