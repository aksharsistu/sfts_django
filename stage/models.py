from django.db import models

from data.models import Line

CHOICES = (
    ('start', 'start'),
    ('end', 'end'),
    ('qa', 'qa'),
    ('rework', 'rework')
)


class StageData(models.Model):
    ipAddress = models.GenericIPAddressField(primary_key=True)
    stageName = models.OneToOneField(Line, on_delete=models.CASCADE)
    placeName = models.CharField(max_length=6, choices=CHOICES)
