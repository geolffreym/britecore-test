from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from itertools import groupby


class RiskTypes(models.Model):
    """
    Model for risk types
    """
    name = models.CharField(max_length=30)
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)


class CustomDataField(models.Model):
    """
    Model specification for arbitrary data fields.
    It allows to elaborate reusable fields.
    """
    TEXT = 'text'
    NUM = 'number'
    DATE = 'date'
    ENUM = 'enum'

    DATA_TYPES = (
        (TEXT, 'Text'),
        (NUM, 'Number'),
        (DATE, 'Date'),
        (ENUM, 'Enumerate')
    )

    label = models.CharField(max_length=64)
    type = models.CharField(max_length=10, choices=DATA_TYPES, default=TEXT)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


class RiskModel(models.Model):
    """
    Model to associate the types of risks and their respective data fields
    """
    risk_type = models.ForeignKey(RiskTypes, on_delete=None, related_name='model_field')
    field = models.ForeignKey(CustomDataField, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def get_fields(risk_id):
        """
        Return a field list by risk id
        :param risk_id: <list> list of risks
        :return:
        """
        risk_model_fields = RiskModel.objects.filter(
            risk_type__pk__in=risk_id
        ).select_related('field', 'risk_type')

        return risk_model_fields.exists() and risk_model_fields or []

    @staticmethod
    def get_serialized_fields(risk_id):
        """
        Return a field list serialized and group by risk id
        :param risk_id: <list> list of risks
        :return:
        """

        # Make a dict with needed data
        risks_types = [{"risk_id": risk.risk_type.pk,
                        "risk": risk.risk_type.name,
                        'label': risk.field.label,
                        'type': risk.field.type,
                        'description': risk.field.description}
                       for risk in RiskModel.get_fields(risk_id)]

        # Group by risk type
        return [{k: list(v)} for k, v in groupby(risks_types, key=lambda x: x['risk'])]
