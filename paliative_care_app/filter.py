import django_filters

from paliative_care_app.models import Prescription


class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Prescription
        fields = ['user',]
