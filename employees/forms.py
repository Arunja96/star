from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    employee_name = forms.CharField(label="Employee Name",max_length=100)
    dob = forms.DateField(label='Date of Birth',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label="Age", required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),)
    gender = forms.ChoiceField(label='Gender',choices=[('male','Male'),('female','Female')],required=False)
    address = forms.CharField(label="Address",max_length=100,required=False)
    country = forms.CharField(label="Country",max_length=100,required=False)
    state = forms.CharField(label="State",max_length=100,required=False)
    city = forms.CharField(label="City",max_length=100,required=False)
    pincode = forms.CharField(label="Pincode",max_length=100,required=False)
    phone_no = forms.IntegerField(label='Phone No',required=False)
    profile_img = forms.ImageField(label='Profile Image', required=False,
                                   widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    username = forms.CharField(label="Username",required=False)
    password = forms.CharField(label="Password",required=False)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Employee
        fields= ['employee_name','dob','age','gender','address','country','state','city','pincode','phone_no','role','team','username','password','email','profile_img']
        exclude = ("created_by",)


    