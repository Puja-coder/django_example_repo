from django.db import models
# Create your models here.

class Employee(models.Model):
    username = models.CharField(blank=False, max_length=254, verbose_name="Name")
    EmployeeID = models.IntegerField(blank=False, verbose_name="EmpID")
    DateOfJoining = models.DateTimeField(blank=False, max_length=254, verbose_name="Joining_date")
