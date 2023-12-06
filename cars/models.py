from django.db import models
class Cars(models.Model):
    brand = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    construction_date = models.DateField()
    motor = models.IntegerField()
    version = models.CharField(max_length=200)