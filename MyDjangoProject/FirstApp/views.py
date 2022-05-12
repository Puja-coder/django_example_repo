from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
import pandas as pd

# Create your views here.
def index(request):
    return HttpResponse("Hello, world! Welcome to my First APP.")

#Save data into database
def save_data(request):
    emp_list = Employee.objects.create(username = "PujaK", EmployeeID = 1001, DateOfJoining = "2022-05-12")
    return HttpResponse("Data Saved Successfully!")

# Using Django ORM
def get_emp_data(request):
    res = list(Employee.objects.values('username', 'EmployeeID', 'DateOfJoining'))
    emp_list = []
    for i in res:
        emp_list.append({"Username ": i['username'], "Employee ID ": i['EmployeeID'], "Date Of Joining ": i['DateOfJoining']})
    return HttpResponse(emp_list)

#Create Panadas DataFrame
def get_dataframe(request):
    emp_list = Employee.objects.values('username', 'EmployeeID', 'DateOfJoining')
    df = pd.DataFrame(emp_list)
    print(df)
    return HttpResponse(df.to_html())

