from django.db import models
from django.contrib.auth.models import User
from  roles.models import Role
from teams.models import Team
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True,default=0)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100,)
    address = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True )
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.CharField(max_length=100,null=True,blank=True )
    phone_no = models.BigIntegerField(null=True,blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    profile_img = models.ImageField(upload_to='employees/profile_images/',null=True,blank=True)

    email = models.EmailField(null=True,blank=True)
    username = models.CharField(max_length=100, null=True,blank=True)
    password = models.CharField(max_length=100, null=True,blank=True)
    access = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,blank=True)

    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.employee_name
    



    
