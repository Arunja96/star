from django.db import models
from employees.models import Employee
# Create your models here.

class Attendence(models.Model):

    employee_name_id = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True, blank=True)
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True)
    checked_date = models.DateField(auto_now_add=True,null=True)

