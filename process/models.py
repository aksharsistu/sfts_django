from django.db import models

from data.models import Line, Product
from stage.models import CHOICES


class Process(models.Model):
    processNo = models.CharField(max_length=6, primary_key=True)
    productCode = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    currentQuantity = models.IntegerField()
    maxQuantity = models.IntegerField()
    tempStartingSno = models.CharField(max_length=12)
    tempEndingSno = models.CharField(max_length=12)
    permStartingSno = models.CharField(max_length=13)
    permEndingSno = models.CharField(max_length=13)


class ProcessCard(models.Model):
    processCardNo = models.CharField(max_length=10, primary_key=True)
    processNo = models.ForeignKey(Process, on_delete=models.CASCADE)
    stageName = models.ForeignKey(Line, on_delete=models.CASCADE)
    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    qa = models.BooleanField(default=False)
    rework = models.BooleanField(default=False)
    final = models.CharField(max_length=6, choices=CHOICES)
    quantity = models.IntegerField()
