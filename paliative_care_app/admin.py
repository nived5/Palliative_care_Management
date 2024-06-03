from django.contrib import admin

from paliative_care_app import models

# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Nurse)
