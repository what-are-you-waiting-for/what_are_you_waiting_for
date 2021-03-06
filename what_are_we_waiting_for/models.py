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


class DischargeType(lookuplists.LookupList):
    pass


class LabTest(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    _title = "Investigation"
    _icon = "fa fa-flask"
    test_type = ForeignKeyOrFreeText(LabTestType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    reviewed_timestamp = fields.DateTimeField(
        null=True, blank=True
    )
    requested = fields.NullBooleanField()
    reviewed = fields.NullBooleanField()


class Imaging(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    _icon = "fa fa-picture-o"
    test_type = ForeignKeyOrFreeText(ImagingTestType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    reviewed_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    reviewed = fields.NullBooleanField()


class SpecialistReview(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    _icon = "fa fa-user-md"
    specialist_type = ForeignKeyOrFreeText(SpecialistType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    reviewed_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    reviewed = fields.NullBooleanField()


class DischargeStep(models.EpisodeSubrecord):
    _angular_service = 'RequestReceive'
    discharge_type = ForeignKeyOrFreeText(DischargeType)
    requested_timestamp = fields.DateTimeField(null=True, blank=True)
    received_timestamp = fields.DateTimeField(null=True, blank=True)
    requested = fields.NullBooleanField()
    transport_type = ForeignKeyOrFreeText(TransportType)
    destination_type = ForeignKeyOrFreeText(DestinationType)
    reviewed = fields.NullBooleanField()
    reviewed_timestamp = fields.DateTimeField(
        null=True, blank=True
    )
