"""
what_are_we_waiting_for models.
"""
from django.db.models import fields
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""


class LabTestType(lookuplists.LookupList):
    pass


class ImagingTestType(lookuplists.LookupList):
    pass


class SpecialistType(lookuplists.LookupList):
    pass
    
    
class TransportType(lookuplists.LookupList):
    pass
    
class DestinationType(lookuplists.LookupList):
    pass

class LabTest(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    test_type = ForeignKeyOrFreeText(LabTestType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    received_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    received = fields.NullBooleanField()


class Imaging(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    test_type = ForeignKeyOrFreeText(ImagingTestType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    received_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    received = fields.NullBooleanField()


class SpecialistReview(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    specialist_type = ForeignKeyOrFreeText(SpecialistType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    received_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    received = fields.NullBooleanField()


class DischargeStep(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    discharge_type = ForeignKeyOrFreeText(TransportType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    received_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    received = fields.NullBooleanField()
