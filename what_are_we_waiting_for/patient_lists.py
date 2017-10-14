"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from what_are_we_waiting_for import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()