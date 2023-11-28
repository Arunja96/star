from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Attendence
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from employees.models import Employee
from django.db.models import Q
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "you have been logged in")
            return redirect('dashboard')
        else:
            messages.success(request,'Your username or password is incorrect...')
            return redirect('index')
    else:
        login_user = request.user.id
        employee = Employee.objects.filter(Q(access=login_user)).first()
        today = timezone.now().date()
        records = Attendence.objects.filter(Q(employee_name_id=employee) & Q(checked_date=today)).first()
        if records:
            check_in_values = records.check_in
            check_out_values = records.check_out
            if bool(check_in_values) and not bool(check_out_values):
                return render(request,'dashboard.html',{'check_in': check_in_values})
            elif bool(check_in_values) and bool(check_out_values):
                return render(request,'dashboard.html',{'check_out': check_out_values,'check_in':check_in_values})
        return render(request, "dashboard.html",{})
    

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logout")
    return redirect('index')

def dashboard(request):
    # employee = Employee.objects.get(id=12)
    login_user = request.user.id
    employee = Employee.objects.filter(Q(access=login_user)).first()
    # Get today's date
    today = timezone.now().date()
    if request.method == "POST":
        today_datetime= datetime.now()
        attendance_records = Attendence.objects.filter(Q(employee_name_id=employee) & Q(checked_date=today)).first()
        if not attendance_records:
            checkin_data = Attendence(employee_name_id=employee, check_in=today_datetime)
            checkin_data.save()
            return render(request,'dashboard.html',{'check_in': today_datetime})
        if attendance_records:
            check_in_values = attendance_records.check_in
            check_out_values = attendance_records.check_out
            if bool(check_in_values) and not bool(check_out_values):
                attendance_records.check_out = today_datetime
                attendance_records.save()
                return render(request,'dashboard.html',{'check_out': today_datetime,'check_in':check_in_values})
    records = Attendence.objects.filter(Q(employee_name_id=employee) & Q(checked_date=today)).first()
    if records:
        check_in_values = records.check_in
        check_out_values = records.check_out
        if bool(check_in_values) and not bool(check_out_values):
            return render(request,'dashboard.html',{'check_in': check_in_values})
        elif bool(check_in_values) and bool(check_out_values):
            return render(request,'dashboard.html',{'check_out': check_out_values,'check_in':check_in_values})
    else:
         return render(request,'dashboard.html',{})
    