from django.db import models


class Line(models.Model):
    line_code = models.CharField(max_length=4, primary_key=True)
    line_description = models.CharField(max_length=20)


class Product(models.Model):
    product_code = models.CharField(max_length=10, primary_key=True)
    fg_code = models.CharField(max_length=10)
    product_description = models.CharField(max_length=20)
    processId = models.CharField(max_length=30)


class Rejection(models.Model):
    rejection_code = models.CharField(max_length=3, primary_key=True)
    rejection_description = models.CharField(max_length=20)


class Rework(models.Model):
    rework_code = models.CharField(max_length=3, primary_key=True)
    rework_description = models.CharField(max_length=20)
