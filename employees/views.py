from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def employees(request):
    records  = Employee.objects.all()
    return render(request,"employees.html",{'records': records})

def employeeform(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                employee_name = form.cleaned_data['employee_name']
                dob = form.cleaned_data['dob']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                address = form.cleaned_data['address']
                country = form.cleaned_data['country']
                state = form.cleaned_data['state']
                city = form.cleaned_data['city']
                pincode = form.cleaned_data['pincode']
                phone_no = form.cleaned_data['phone_no']
                role = form.cleaned_data['role']
                team =form.cleaned_data['team']
                username = form.cleaned_data['username']
                password =form.cleaned_data['password']
                email =form.cleaned_data['email']
                profile =form.cleaned_data['profile_img']
                if username and password and email:
                    user_create = User.objects.create_user(username=username, password=password,email=email)
                    user_create.save()
                else:
                    user_create = None

                save_record = Employee(employee_name=employee_name,dob=dob,age=age,gender=gender,address=address,country=country,state=state,
                                       city=city,pincode=pincode,phone_no=phone_no,role=role,team=team,username=username, password=password,email=email,access=user_create,profile_img=profile)
                save_record.save()
                messages.success(request, "Record Created Successfully")
                return redirect('employees')
        form = EmployeeForm()
        return render(request,"employee_form.html",{'form': form})
    else:
        messages.success('you not logged in')
        return redirect('index')


def view_record(request,pk):
    if request.user.is_authenticated:
        form = EmployeeForm()
        record = Employee.objects.get(id=pk)
        return render(request, "view_employee.html",{'record': record,'form':form})
    else:
        messages.success('you not logged in')
        return redirect('index')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        view_record = Employee.objects.get(id=pk)
        view_record.delete()
        return redirect('employees')
    else:
        messages.success('you not logged in')
        return redirect('index')
    
def update_record(request,  pk):
    if request.user.is_authenticated:
        current_record = Employee.objects.get(id=pk)
        if request.method == 'POST':
            form = EmployeeForm(request.POST, request.FILES, instance=current_record)  # Pass request.FILES here
            if form.is_valid():
                if not current_record.access:
                    username = form.cleaned_data['username']
                    password =form.cleaned_data['password']
                    email =form.cleaned_data['email']
                    if username and password and email:
                        user_create = User.objects.create_user(username=username, password=password,email=email)
                        user_create.save()
                        # Update current_record.access with the ID of the newly created User
                        current_record.access = user_create
                        current_record.save()
                profile =form.cleaned_data['profile_img']
                form.save()
                messages.success(request, "Record Updated Successfully")
                return redirect('employees')
        else:
            # It's a GET request or a form with errors, initialize the form without data
            form = EmployeeForm(instance=current_record)
            return render(request, "update_employee.html", {'form': form})
    else:
        messages.success('you not logged in')
        return redirect('index')